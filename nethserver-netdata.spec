Summary: NethServer netdata module
Name: nethserver-netdata
Version: 0.0.1
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
