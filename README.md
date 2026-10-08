# oocolrm: Sovereign COLUMN STRIPPER

<div align="center">

```
================================================================================
                                oocolrm
               Sovereign openOODA COLUMN STRIPPER
================================================================================
```

**Sovereign COLUMN STRIPPER**  
*Strips character columns from line streams using precise byte column boundaries.*  
*Two Faces, One Engine:* Modern terminal ergonomics for humans • Zero-leakage MCP for AI agents  
Written in 100% pure [openOODA](https://github.com/openOODA).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Architecture: x86_64 | aarch64](https://img.shields.io/badge/Arch-x86__64%20%7C%20aarch64-lightgrey.svg)]()

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64 & aarch64)
```bash
curl -fsSL https://openooda-tools.github.io/oocolrm/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (AUR / PKGBUILD)
yay -S oocolrm-bin
# Or manual PKGBUILD:
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openooda-tools.github.io/oocolrm/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openooda-tools.github.io/oocolrm/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
oocolrm-uninstall
# or: curl -fsSL https://openooda-tools.github.io/oocolrm/uninstall.sh | bash
```

---

## 2. CLI Usage

```
usage: oocolrm [options] [start [stop]] [FILE]

Remove selected columns from each line of a file or standard input.

Options:
  -s, --start NUM        starting column index (1-based)
  -e, --stop NUM         ending column index inclusive
  -x, --expand-tabs      expand tabs to column spaces before stripping
  -t, --tab NUM          tab stop width [default: 8]
  -r, --replace CHAR     replace stripped columns with character instead of deletion
  -v, --invert           invert range: keep selected columns, strip the rest
      --inspect          display execution statistics summary
      --demo             run demonstration scenario with synthetic log data
      --json             output formatted as JSON telemetry
  -h, --help             display this help and exit
  -V, --version          output version information and exit
      --mcp              run as Model Context Protocol stdio server
```

### Examples

```bash
# Strip column 5 to end of line from each row
oocolrm 5 < file.txt

# Remove columns 4 through 7 inclusive
oocolrm 4 7 file.txt

# Remove first 3 columns
oocolrm 1 3 file.txt

# Expand tabs and strip columns 10 through 20
oocolrm 10 20 -x -t 8 file.txt

# Replace columns 5 through 10 with '.' (masking sensitive data)
oocolrm 5 10 -r "." file.txt

# Invert selection (keep only columns 4 through 8, remove the rest)
oocolrm 4 8 -v file.txt

# Run demonstration with telemetry
oocolrm --demo --json
```

---

## 3. Model Context Protocol (MCP)

When invoked with `--mcp`, `oocolrm` operates as a JSON-RPC 2.0 stdio server providing sovereign column manipulation tools for AI agents without network authority:

```bash
oocolrm --mcp
```

### Exposed MCP Tools

1. **`colrm_strip`**: Strip 1-indexed column range `[start, stop]` from each line of text.
2. **`colrm_slice`**: Extract and keep only specified column range from each line (inverted excision).
3. **`colrm_replace`**: Replace specified column range with recurring filler characters.
4. **`colrm_inspect`**: Inspect lines with a terminal column ruler and before/after character metrics.
5. **`colrm_stats`**: Stream text through column stripper and return aggregate metrics in JSON.

---

## 4. Security & Zero Ambient Authority

* **Pure Capability Bounded:** Operates strictly with explicit tokens (`&FsReadCap`, `&ProcessCap`, `&EnvCap`). Zero ambient authority or network egress.
* **Negative-Trust Architecture:** Strict boundary validation on 1-indexed columns, tab calculations, and line buffers.
* **Hermetic Binary:** Standalone zero-dependency executable.

---

## 5. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
