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
license = "L-KDIY-CJHJCJ"
path = "/usr/share/%{name}-%{version}/" .. "license/" .. license
print("Your licenses have been installed in " .. path)
locale = io.popen("locale | grep LANG= | cut -d'=' -f2 | cut -d'_' -f1"):read("*all")
print("System locale: " .. locale)
lpath= path .. "/UTF8/LA_" .. locale
locale = io.popen("less " .. lpath):read("*all")
print(locale)
io.write("Please read the relevant version and agree that you will be bound to its provisions: Type YES or NO ")
answer = io.read()
if answer == "NO" then
  os.remove("/usr/share/%{name}-%{version}/license/accept")
  print("License not accepted. If you want to accept the license. touch " .. path .. "/accept")
  print("Then proceed with install")
else
  print("License accepted. Proceed with install")
end

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}/usr/share/%{name}-%{version}/license/
tar zxf %{SOURCE0} --directory %{buildroot}/usr/share/%{name}-%{version}/license
echo "I agree to be bound by the terms" > %{buildroot}/usr/share/%{name}-%{version}/license/accept

%files
/usr/share/%{name}-%{version}/*

%changelog
* Tue Feb  7 2023 Christina Meno <Christina.Meno@ibm.com>
- 
