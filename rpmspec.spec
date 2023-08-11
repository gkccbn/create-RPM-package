name:netflow2ng	
Version:1
	
Release:0	
Summary:rpm for git	

Group: System Environment/Base		
License:MIT	
URL:https://github.com/synfinatic/netflow2ng		
Source0:netflow2ng-1.tar.gz
buildRoot:%{_tmppath}/%{name}-buildroot

	
BuildRequires:golang
BuildRequires:git
BuildRequires:make


%description
RPM package for labris

%prep
%setup -q
%global debug_package %{nil}

%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin


#install -d $RPM_BUILD_ROOT/usr/bin
echo $RPM_BUILD_ROOT

install -D dist/netflow2ng-0.0.4 $RPM_BUILD_ROOT/usr/bin

%files

%doc
%{_bindir}/netflow2ng-0.0.4
