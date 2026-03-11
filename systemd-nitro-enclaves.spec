%bcond check 1

Name:           systemd-nitro-enclaves
Version:        0.1.0
Release:        1%{?dist}
Summary:        AWS Nitro Enclaves systemd services

License:        Apache-2.0
URL:            https://github.com/virtee/systemd-nitro-enclaves
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  systemd-rpm-macros

%global _description %{expand:
systemd services for AWS Nitro Enclaves.}

%description %{_description}

%prep
%autosetup -n %{name}-%{version}

%build
# nothing

%install
%make_install PREFIX=%{buildroot}

%post
%systemd_post nitro-enclaves-allocator.service

%preun
%systemd_preun nitro-enclaves-allocator.service

%postun
%systemd_postun_with_restart nitro-enclaves-allocator.service

%files
%license LICENSE
%{_unitdir}/nitro-enclaves-allocator.service
%{_sysconfdir}/nitro_enclaves
%{_sysconfdir}/nitro_enclaves/allocator.yaml
%{_libexecdir}/nitro-enclaves-allocator

%changelog
* Fri Feb 20 2026 Tyler Fanelli <tfanelli@redhat.com> - 0.1.0-1
- Initial version for Fedora review.
