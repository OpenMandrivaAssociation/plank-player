%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Full screen media player with remote control interface
Name:		plank-player
Version:	5.27.0
Release:	1
License:	LGPL
Group:		System/Libraries
Url:		http://plasma-bigscreen.org/
Source0:	http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5QuickControls2)
BuildRequires:	pkgconfig(Qt5Multimedia)
Suggests:	plasma-bigscreen
Suggests:	plasma-remotecontrollers
Supplements:	plasma-bigscreen

%description
Full screen media player with remote control interface

%files -f %{name}.lang
%{_bindir}/plank-player
%{_datadir}/applications/org.plank.player.desktop
%{_datadir}/icons/hicolor/*/apps/plank-player.png
%{_datadir}/metainfo/org.kde.invent.plank_player.metainfo.xml

#----------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name
