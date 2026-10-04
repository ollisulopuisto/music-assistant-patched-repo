#!/bin/bash
set -euo pipefail

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
install_prefix="${1:-$HOME/.local/opt/mpd-native}"
brew_prefix="$(brew --prefix)"
mpd_build_dir="$(mktemp -d "${TMPDIR:-/tmp}/mpd-native.XXXXXX")"
trap 'rm -rf "$mpd_build_dir"' EXIT

curl --fail --location --proto '=https' --tlsv1.2 \
  https://www.musicpd.org/download/mpd/0.24/mpd-0.24.15.tar.xz \
  --output "$mpd_build_dir/mpd.tar.xz"
printf '%s  %s\n' \
  524c70bce3fcd268016156bdc97abcf5be1904f0c6fd622688999123e3c4c457 \
  "$mpd_build_dir/mpd.tar.xz" | shasum -a 256 -c -
tar -xf "$mpd_build_dir/mpd.tar.xz" -C "$mpd_build_dir"
source_dir="$mpd_build_dir/mpd-0.24.15"
for patch_path in "$repo_root"/native-mpd/patches/*.patch; do
  git -C "$source_dir" apply --check "$patch_path"
  git -C "$source_dir" apply "$patch_path"
done

c++ -std=c++20 -I"$source_dir/src" \
  "$repo_root/native-mpd/tests/frame-alignment.cxx" \
  -o "$mpd_build_dir/frame-alignment"
if "$mpd_build_dir/frame-alignment" original; then
  echo 'Expected original byte-write implementation to fail the regression' >&2
  exit 1
fi
"$mpd_build_dir/frame-alignment"

export PKG_CONFIG_PATH="$brew_prefix/lib/pkgconfig:$(brew --prefix icu4c)/lib/pkgconfig${PKG_CONFIG_PATH:+:$PKG_CONFIG_PATH}"
meson setup "$mpd_build_dir/build" "$source_dir" \
  --prefix="$install_prefix" \
  -Ddocumentation=disabled -Dtest=false -Dauto_features=disabled \
  -Dcurl=enabled -Dffmpeg=enabled -Dflac=enabled -Ddsd=true \
  -Dicu=enabled -Dlibsamplerate=enabled -Dsoxr=enabled \
  -Ddefault_library=static -Dbuildtype=debugoptimized
meson compile -C "$mpd_build_dir/build" -j 6
meson install -C "$mpd_build_dir/build" --no-rebuild
