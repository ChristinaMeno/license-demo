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

%post -p <lua>
print("Your licenses have been installed in /usr/source/%{name}-%{version}/")
io.write("Please read the relevant version and agree that you will be bound to its provisions: Type YES or NO ")
answer = io.read()
if answer == "NO" then
  os.remove("/usr/share/%{name}-%{version}/accept")
  print("File deleted successfully.")
else
  print("File not deleted.")
end

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}/usr/share/%{name}-%{version}
tar zxf %{SOURCE0} --directory %{buildroot}/usr/share/%{name}-%{version}
echo "I agree to be bound by the terms" > %{buildroot}/usr/share/%{name}-%{version}/accept

%files
/usr/share/%{name}-%{version}/English.txt
/usr/share/%{name}-%{version}/Greek.txt
/usr/share/%{name}-%{version}/accept

%changelog
* Tue Feb  7 2023 Christina Meno <Christina.Meno@ibm.com>
- 
