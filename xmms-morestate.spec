%define name xmms-morestate
%define version 1.2
%define release %mkrel 9

Summary: Maintain xmms state information
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/xmms-morestate/%{name}-%{version}.tar.bz2
Patch: xmms-morestate-1.2-no-x86.patch
URL: http://sourceforge.net/projects/xmms-morestate/
License: GPL
Group: Sound
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libxmms-devel
Requires: xmms
Provides: xmms_morestate
Obsoletes: xmms_morestate

%description
The XMMS Morestate/Autoplay plugin restores some additional settings:
volume (esd only), song time, and playing/paused status.

It can also make XMMS start playing on start. It can start at the
beginning of the playlist, at a random position or at the position the
last XMMS-Session stopped.

%prep
%setup -q
%patch -p1
aclocal
autoconf
automake

%build
export CC="gcc -fPIC"
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm  -f %buildroot%_libdir/xmms/General/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS README TODO ChangeLog
%_libdir/xmms/General/libmorestate.so


