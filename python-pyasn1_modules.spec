
%define		module	pyasn1-modules

Summary:	ASN.1 tools for Python
Summary(pl.UTF-8):	Narzędzia ASN.1 dla Pythona
Name:		python-pyasn1_modules
Version:	0.0.2
Release:	2
License:	BSD-like
Group:		Libraries/Python
Source0:	http://downloads.sourceforge.net/pyasn1/%{module}-%{version}.tar.gz
# Source0-md5:	adc49aee6603a162f9d4a6830c8dc470
URL:		http://pyasn1.sourceforge.net/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python >= 1:2.5
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	python-pyasn1 >= 0.0.13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a small but growing collection of ASN.1 data structures
expressed in Python terms using pyasn1 data model.

It's thought to be useful to protocol developers and testers.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_install

find $RPM_BUILD_ROOT%{py_sitescriptdir} -type f -name "*.py" | xargs rm
cp tools/*.py $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%{py_sitescriptdir}/pyasn1_modules
%{py_sitescriptdir}/*.egg-info
%{_examplesdir}/*
