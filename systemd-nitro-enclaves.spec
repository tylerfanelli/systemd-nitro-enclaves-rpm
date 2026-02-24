%bcond check 1
%global debug_package %{nil}

Name:           systemd-nitro-enclaves
Version:        0.1.0
Release:        1%{?dist}
Summary:        AWS Nitro Enclaves systemd services

License:        Apache-2.0
URL:            https://github.com/virtee/systemd-nitro-enclaves.git
Source0:        %{name}-%{version}.tar.gz

# Nitro enclaves are only available on x86_64 and aarch64 instances.
ExclusiveArch:  x86_64 aarch64

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

%files
%license LICENSE
%{_unitdir}/nitro-enclaves-allocator.service
%{_bindir}/nitro-cli-config
%{_bindir}/nitro-enclaves-allocator
%{_sysconfdir}/nitro_enclaves
%{_sysconfdir}/nitro_enclaves/allocator.yaml

%changelog
* Fri Feb 20 2026 Tyler Fanelli <tfanelli@redhat.com> - 0.1.0-1
- Initial version for Fedora review.
