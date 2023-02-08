Name:           ibm-storage-ceph-license
Version:        5.3 
Release:        1%{?dist}
Summary:        IBM ceph license 

License:       IBM 
URL:           ibm.com 
Source0:       license.tar.gz

BuildRequires: bash 

%description
there are licenses here

%pretrans -p <lua>
print("Your licenses have been installed in /usr/source/%{name}-%{version}/")
io.write("Please read the relevant version and agree that you will be bound to its provisions: Type YES or NO ")
answer = io.read()
print(answer)

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}/usr/source/%{name}-%{version}
tar zxf %{SOURCE0} --directory %{buildroot}/usr/source/%{name}-%{version}

%files
/usr/source/%{name}-%{version}/English.txt
/usr/source/%{name}-%{version}/Greek.txt

%changelog
* Tue Feb  7 2023 Christina Meno <Christina.Meno@ibm.com>
- 
