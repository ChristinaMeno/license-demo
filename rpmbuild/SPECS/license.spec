Name:           ibm-storage-ceph-license
Version:        5.3 
Release:        1%{?dist}
Summary:        IBM ceph license 

License:       IBM 
URL:           ibm.com 
Source0:       license.tar.gz

BuildArch: noarch
BuildRequires: bash 

%description
there are licenses here

%post -p <lua>
accept_eula = os.getenv("ACCEPT_EULA")
if accept_eula then
  accept_eula = accept_eula:lower():gsub("\n", "")
end


if not (accept_eula == "yes" or accept_eula == "y") then
	license = "L-KDIY-CJHJCJ"
	path = "/usr/share/%{name}-%{version}/" .. "license/" .. license
	print("\nYour licenses have been installed in " .. path)
	locale = io.popen("locale | grep LANG= | cut -d'=' -f2 | cut -d'_' -f1"):read("*all"):gsub("\n", "")
	print("System locale: " .. locale)
	lpath= path .. "/UTF8/LA_" .. locale
	agreement, err = io.open(lpath, 'r')
	if agreement then
	  print(agreement:read("a"))
	else
	  print(err)
	end

	io.write("\nYou can read this license in another language at " .. path)
	io.write("\nAccept these provisions: Type YES or NO ")
	answer = io.read():lower()

	if not (answer == "yes" or answer == "y") then
	  os.remove("/usr/share/%{name}-%{version}/license/accept")
	  print("\nLicense not accepted.")
	  print("\nWhen you are ready to accept the license. run `sudo touch " .. path .. "/accept`")
	  print("\nThen proceed with install")
	else
	  print("\nLicense accepted.") 
	  print("\nProceed with install")
	end
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
