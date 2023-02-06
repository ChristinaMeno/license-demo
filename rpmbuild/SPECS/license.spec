Name:           license
Version:        5.3 
Release:        1%{?dist}
Summary:        Licenses for IBM storage ceph 

License:       IBM 
URL:           ibm.com 
Source0:       license.tar.gz

BuildRequires: bash 

%description


%prep
%autosetup


%build
%configure
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%license add-license-file-here
%doc add-docs-here


%pretrans

if [ ${ACCEPT_EULA} != "y" ]
then
  echo "The license terms for this product can be downloaded from"
  echo "https://licr.dal1a.cirrus.ibm.com/ui/#/licensefiles/L-KDIY-CJHJCJ"
  echo "The license terms are available offline by installing the ibm-legal-mumbojumbo package"
  echo "and navigating to /var/lib/docs/legalstuffs"
  echo
  read "Do you accept the license terms? (Enter YES or NO)" ANS
  if [ ${ANS} != "YES" ];
  then
    exit
  fi
fi

%changelog
* Mon Feb  6 2023 vagrant
- 
