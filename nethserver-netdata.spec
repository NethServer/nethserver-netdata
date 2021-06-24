Summary: NethServer netdata module
Name: nethserver-netdata
Version: 2.0.2
Release: 1%{?dist}
License: GPL
Source0: %{name}-%{version}.tar.gz
URL: %{url_prefix}/%{name}
BuildArch: noarch

Requires: netdata
Requires: nethserver-base

BuildRequires: nethserver-devtools

%description
netdata module for NethServer.

%prep
%setup -q

%build
perl createlinks

%install
rm -rf %{buildroot}
(cd root ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-%{release}-filelist

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog
* Thu Jun 24 2021 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 2.0.2-1
- netdata update config overwrite - Bug NethServer/dev#6528

* Thu Feb 18 2021 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 2.0.1-1
- netdata web interface inaccessible - Bug - NethServer/dev#6429

* Wed Nov 18 2020 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 2.0.0-1
- Install netdata by default - NethServer/dev#6333

* Wed Apr 10 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.0-1
- Support netdata 1.13 from EPEL

* Wed Mar 27 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1
- First release

