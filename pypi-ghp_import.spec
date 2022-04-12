#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-ghp_import
Version  : 2.0.2
Release  : 3
URL      : https://files.pythonhosted.org/packages/13/b8/8dd1ea116774415b785c7c2e4bf91c2c50b5eae577bcc2d2a095c2ce20fd/ghp-import-2.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/13/b8/8dd1ea116774415b785c7c2e4bf91c2c50b5eae577bcc2d2a095c2ce20fd/ghp-import-2.0.2.tar.gz
Summary  : Copy your docs directly to the gh-pages branch.
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-ghp_import-bin = %{version}-%{release}
Requires: pypi-ghp_import-license = %{version}-%{release}
Requires: pypi-ghp_import-python = %{version}-%{release}
Requires: pypi-ghp_import-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(python_dateutil)

%description
GitHub Pages Import
===================
[![CI status](https://github.com/davisp/ghp-import/workflows/CI/badge.svg)](https://github.com/davisp/ghp-import/actions?query=workflow%3Aci)
[![CircleCI](https://circleci.com/gh/c-w/ghp-import/tree/master.svg?style=svg)](https://circleci.com/gh/c-w/ghp-import/tree/master)
[![TravisCI](https://travis-ci.org/c-w/ghp-import.svg?branch=master)](https://travis-ci.org/c-w/ghp-import)

%package bin
Summary: bin components for the pypi-ghp_import package.
Group: Binaries
Requires: pypi-ghp_import-license = %{version}-%{release}

%description bin
bin components for the pypi-ghp_import package.


%package license
Summary: license components for the pypi-ghp_import package.
Group: Default

%description license
license components for the pypi-ghp_import package.


%package python
Summary: python components for the pypi-ghp_import package.
Group: Default
Requires: pypi-ghp_import-python3 = %{version}-%{release}

%description python
python components for the pypi-ghp_import package.


%package python3
Summary: python3 components for the pypi-ghp_import package.
Group: Default
Requires: python3-core
Provides: pypi(ghp_import)
Requires: pypi(python_dateutil)

%description python3
python3 components for the pypi-ghp_import package.


%prep
%setup -q -n ghp-import-2.0.2
cd %{_builddir}/ghp-import-2.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649751281
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-ghp_import
cp %{_builddir}/ghp-import-2.0.2/LICENSE %{buildroot}/usr/share/package-licenses/pypi-ghp_import/872afb38a84918b99ae98ac95bbf7ac956af53e5
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ghp-import

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-ghp_import/872afb38a84918b99ae98ac95bbf7ac956af53e5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
