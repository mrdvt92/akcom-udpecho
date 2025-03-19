%global debug_package %{nil}

Name: akcom-udpecho
Summary: UDP echo server/client with support for TR-143 UDPEchoPlus
Epoch:   1
Version: 0.6
Release: 3%{?dist}
License: Modified BSD License
Url: https://github.com/alaskacommunications/akcom-udpecho/
Source0: https://github.com/alaskacommunications/akcom-udpecho/releases/akcom-udpecho-%{version}.tar.gz
Group: System Environment/Daemons

Requires: glibc
BuildRequires: glibc-devel make gcc which libtool autoconf automake file diffutils gzip xz

%description
akcom-udpecho is a shell utility for testing UDP echo servers. akcom-udpecho
supports for RFC 862 compliant servers and TR-143 UDPEchoPlus compliant
servers.  If the UDP Echo variant is not specified, akcom-udpecho will
attempt to determine the variant by examining the TestRespSN,
TestRespRecvTimeStamp, and TestRespReplyTimeStamp fields of the UDPEchoPlus
packet for non-zero values.

%prep
%setup -q

%build
%configure \
   --prefix=/usr \
   --mandir=/usr/share/man \
   --docdir=/usr/share/doc/securecoreutils-%{version} \
   CPPFLAGS=-Wno-unknown-pragmas

%{__make} %{?_smp_mflags}

strip src/akcom-udpecho
strip src/akcom-udpechod

%install
%{__make} DESTDIR=%{buildroot} install
mkdir -p                  %{buildroot}/%{_unitdir}/
cp akcom-udpechod.service %{buildroot}/%{_unitdir}/

%files
%attr(0755,root,root) %{_bindir}/akcom-udpecho
%attr(0755,root,root) %{_sbindir}/akcom-udpechod
%attr(0644,root,root) %{_mandir}/man1/akcom-udpecho.1.gz
%attr(0644,root,root) %{_mandir}/man8/akcom-udpechod.8.gz
%attr(0755,root,root) %{_unitdir}/akcom-udpechod.service

%check
%{__make} check

%changelog
