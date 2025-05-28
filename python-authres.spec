#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module
%bcond_without	tests	# doctests

%define		module		authres
Summary:	Authentication Results Header Module
Summary(pl.UTF-8):	Moduł nagłówków Authentication Results
Name:		python-%{module}
Version:	1.2.0
Release:	3
License:	Apache v2.0
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/a/authres/%{module}-%{version}.tar.gz
# Source0-md5:	b24ee2541d74eac661fde5c8c27da689
URL:		https://launchpad.net/authentication-results-python
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package for parsing "Authentication-Results" headers as defined in RFC
5451.

%description -l pl.UTF-8
Pakiet do analizy nagłówków "Authentication-Results", zdefiniowanych w
RFC 5451.

%package -n python3-%{module}
Summary:	Authentication Results Header Module
Summary(pl.UTF-8):	Moduł nagłówków Authentication Results
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-%{module}
Package for parsing "Authentication-Results" headers as defined in RFC
5451.

%description -n python3-%{module} -l pl.UTF-8
Pakiet do analizy nagłówków "Authentication-Results", zdefiniowanych w
RFC 5451.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m authres
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m authres
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES README
%{py_sitescriptdir}/authres
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES README
%{py3_sitescriptdir}/authres
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
