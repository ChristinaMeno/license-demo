Name: adm
Version: 1.0
Release: 1%{?dist}
Summary: The adm package

License: GPLv2
URL: https://example.com/adm

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The adm package is an example package for demonstration purposes.

%build
# No build step required for this package

%pretrans 
if [ -z "$ACCEPT_EULA" ]; then
	if [ ! -f /usr/share/ibm-storage-ceph-license-5.3/license/accept ]; then
	  echo "The license agreement has not been accepted. Exiting."
	  exit 1
	else
	  echo "The license agreement found. Continuing."
	fi
fi

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}/usr/share/%{name}-%{version}

%files
%dir /usr/share/%{name}-%{version}

%changelog
* Tue Feb  7 2023 Christina Meno <Christina.Meno@ibm.com>
- Initial release.

