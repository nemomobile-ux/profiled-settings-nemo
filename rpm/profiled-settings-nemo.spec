Name:       profiled-settings-nemo

Summary:    profiled configuration for Nemo
Version:    0.0.2
Release:    1
Group:      System/Library
License:    LGPL 2.1
BuildArch:  noarch
URL:        https://github.com/nemomobile-ux/profiled-settings-nemo
Source0:    %{name}-%{version}.tar.gz
Requires:   profiled
Conflicts:  profiled-settings-default
Provides:   profiled-settings

%description
profiled configuration for Nemo

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}/%{_sysconfdir}/profiled/
install -m 644 ini/* %{buildroot}/%{_sysconfdir}/profiled/

%files
%defattr(-,root,root,-)
%doc COPYING
%{_sysconfdir}/profiled/
