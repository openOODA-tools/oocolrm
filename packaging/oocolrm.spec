Name:           oocolrm
Version:        0.1.0
Release:        1%{?dist}
Summary:        Strips character columns from line streams using precise byte column boundaries.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oocolrm
Source0:        oocolrm-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oocolrm is a sovereign, capability-bounded COLUMN STRIPPER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oocolrm
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oocolrm-uninstall

%files
/usr/bin/oocolrm
/usr/bin/oocolrm-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
