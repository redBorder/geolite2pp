%global upstream_name libgeolite
%global debug_package %{nil}
%define _unpackaged_files_terminate_build 0

Summary:	GeoLite lib
Name:		libgeolite
Version:	%{__version}
Release:	1%{?dist}
License:	Apache 2
Source0: %{name}-%{version}.tar.gz

BuildRequires:	libmaxminddb-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-c++
BuildRequires:	cmake

%description
Snort 3 libgeolite

%package modules
Summary:	Libgeolite for geoip enrichment in snort

%description modules
Libgeolite for geoip enrichment in snort

%package devel
Summary:	Development libraries and headers for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries and headers for %{name}.

%prep
%autosetup -n %{upstream_name}-%{version}

%build
mkdir build
cd build
cmake ..
make

%install
mkdir -p %{buildroot}/usr/local
cd build
make DESTDIR=%{buildroot} install

%ldconfig_scriptlets

%files
/usr/local/lib/libgeolite2++.so
/usr/local/bin/geolite2pp_get_database.sh

%files devel
/usr/local/lib/libgeolite2++.a
/usr/local/include/GeoLite2PP.hpp
/usr/local/include/GeoLite2PP_error_category.hpp
/usr/local/include/GeoLite2PP_version.hpp

%changelog
