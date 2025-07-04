#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_without	tests	# unit tests

Summary:	ASN.1 modules for Python 2
Summary(pl.UTF-8):	Moduły ASN.1 dla Pythona 2
Name:		python-pyasn1_modules
# keep 0.3.x here for python2 support
Version:	0.3.0
Release:	1
License:	BSD-like
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pyasn1-modules/
Source0:	https://files.pythonhosted.org/packages/source/p/pyasn1-modules/pyasn1_modules-%{version}.tar.gz
# Source0-md5:	94ee572b06ae09f1903b11333575b091
URL:		https://github.com/etingof/pyasn1-modules
%if %{with python2}
BuildRequires:	python >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pyasn1 >= 0.4.7
BuildRequires:	python-pyasn1 < 0.6.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:3.6
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pyasn1 >= 0.4.7
BuildRequires:	python3-pyasn1 < 0.6.0
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a small but growing collection of ASN.1 data structures
expressed in Python terms using pyasn1 data model.

It's thought to be useful to protocol developers and testers.

%description -l pl.UTF-8
Ten pakiet to mała, ale wciąż rosnąca kolekcja struktur danych ASN.1
wyrażona w Pythonie przy użyciu modelu danych pyasn1.

Jest rozwijana z myślą o programistach i testerach protokołów.

%package -n python3-pyasn1_modules
Summary:	ASN.1 modules for Python 2
Summary(pl.UTF-8):	Moduły ASN.1 dla Pythona 2
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.6
Obsoletes:	python3-pyasn1-modules < 0.2.1-2

%description -n python3-pyasn1_modules
This is a small but growing collection of ASN.1 data structures
expressed in Python terms using pyasn1 data model.

It's thought to be useful to protocol developers and testers.

%description -n python3-pyasn1_modules -l pl.UTF-8
Ten pakiet to mała, ale wciąż rosnąca kolekcja struktur danych ASN.1
wyrażona w Pythonie przy użyciu modelu danych pyasn1.

Jest rozwijana z myślą o programistach i testerach protokołów.

%prep
%setup -q -n pyasn1_modules-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp tools/*.py $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__sed} -i -e '1s,/usr/bin/env python,%{__python},' $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/*.py
%endif

%if %{with python3}
%py3_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-pyasn1_modules-%{version}
cp tools/*.py $RPM_BUILD_ROOT%{_examplesdir}/python3-pyasn1_modules-%{version}
%{__sed} -i -e '1s,/usr/bin/env python,%{__python3},' $RPM_BUILD_ROOT%{_examplesdir}/python3-pyasn1_modules-%{version}/*.py
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.txt LICENSE.txt README.md
%{py_sitescriptdir}/pyasn1_modules
%{py_sitescriptdir}/pyasn1_modules-%{version}-py*.egg-info
%{_examplesdir}/%{name}-%{version}
%endif

%if %{with python3}
%files -n python3-pyasn1_modules
%defattr(644,root,root,755)
%doc CHANGES.txt LICENSE.txt README.md
%{py3_sitescriptdir}/pyasn1_modules
%{py3_sitescriptdir}/pyasn1_modules-%{version}-py*.egg-info
%{_examplesdir}/python3-pyasn1_modules-%{version}
%endif
