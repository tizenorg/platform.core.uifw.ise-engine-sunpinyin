Name:       ise-engine-sunpinyin
Summary:    Chinese Pinyin ISE
Version:    1.0.2
Release:    1
Group:      Graphics & UI Framework/Input
License:    LGPL-2.1+ and CDDL-1.0
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  prelink
BuildRequires:  pkgconfig(isf)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(ecore-imf)
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig


%description
Chinese Pinyin Engine ISE and it has been supported by Input Service Framework(ISF).

%package devel
Summary:    Chinese Pinyin ISE header files
Group:      Development/Libraries

%description devel
This package contains Chinese Pinyin engine ISE header files and static libraries for Soft ISE development.

%prep
%setup -q

%build
./bootstrap
%configure  --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}%{_datadir}/license
install -m0644 %{_builddir}/%{buildsubdir}/LGPL.LICENSE %{buildroot}%{_datadir}/license/%{name}
cat %{_builddir}/%{buildsubdir}/OPENSOLARIS.LICENSE >> %{buildroot}%{_datadir}/license/%{name}
install -m0644 %{_builddir}/%{buildsubdir}/LGPL.LICENSE %{buildroot}%{_datadir}/license/%{name}-devel
cat %{_builddir}/%{buildsubdir}/OPENSOLARIS.LICENSE >> %{buildroot}%{_datadir}/license/%{name}-devel

%define __debug_install_post   \
    %{_rpmconfigdir}/find-debuginfo.sh %{?_find_debuginfo_opts} "%{_builddir}/%{?buildsubdir}"\
%{nil}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_datadir}/scim/icons/sunpinyin_logo.png
%{_datadir}/scim/ise-engine-sunpinyin/*
%{_datadir}/packages/*
%{_libdir}/scim-1.0/1.4.0/IMEngine/ise-engine-sunpinyin.so
%{_libdir}/libsunpinyin*.so
/usr/share/license/%{name}

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/pkgconfig/sunpinyin-2.0.pc
/usr/share/license/%{name}-devel
