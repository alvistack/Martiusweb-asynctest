# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-asynctest
Epoch: 100
Version: 0.13.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Enhance unittest package with testing asyncio libraries
License: Apache-2.0
URL: https://github.com/Martiusweb/asynctest/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
The package asynctest is built on top of the standard unittest module
and cuts down boilerplate code when testing libraries for asyncio.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-asynctest
Summary: Enhance unittest package with testing asyncio libraries
Requires: python3
Provides: python3-asynctest = %{epoch}:%{version}-%{release}
Provides: python3dist(asynctest) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-asynctest = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(asynctest) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-asynctest = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(asynctest) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-asynctest
The package asynctest is built on top of the standard unittest module
and cuts down boilerplate code when testing libraries for asyncio.

%files -n python%{python3_version_nodots}-asynctest
%license LICENSE.md
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-asynctest
Summary: Enhance unittest package with testing asyncio libraries
Requires: python3
Provides: python3-asynctest = %{epoch}:%{version}-%{release}
Provides: python3dist(asynctest) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-asynctest = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(asynctest) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-asynctest = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(asynctest) = %{epoch}:%{version}-%{release}

%description -n python3-asynctest
The package asynctest is built on top of the standard unittest module
and cuts down boilerplate code when testing libraries for asyncio.

%files -n python3-asynctest
%license LICENSE.md
%{python3_sitelib}/*
%endif

%changelog
