%define module cyclonedx-python-lib
%define oname cyclonedx_python_lib

Name:		python-cyclonedx-python-lib
Version:	11.6.0
Release:	1
Summary:	Python library for CycloneDX
Group:		Development/Python
License:	Apache-2.0
URL:		https://pypi.org/project/cyclonedx-python-lib/
Source0:	https://files.pythonhosted.org/packages/source/c/%{module}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(wheel)

%description
Python library for CycloneDX

%files
%{py_sitedir}/cyclonedx
%{py_sitedir}/%{oname}-%{version}.dist-info
