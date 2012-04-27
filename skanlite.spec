Name:		skanlite
Version:	0.8
Release:	1
License:	GPLv2+
Url:		http://opendesktop.org/content/show.php/Skanlite?content=109803
Group:		Graphical desktop/KDE
Source0:	http://sourceforge.net/projects/sanewidget/files/Skanlite/%name-%version.tar.bz2
Summary:        An image scanning application
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  libksane-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	libpng-devel

%description
Skanlite is an image scanning application that does nothing more than
scan and save images. It is based on libksane, a KDE interface for SANE
library to control flat scanners.

%if %mdkversion < 200900
%post
%{update_desktop_database}
%update_icon_cache hicolor

%postun
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif

%files -f %name.lang
%defattr(-,root,root)
%_kde_bindir/*
%_kde_datadir/applications/kde4/*.desktop

#------------------------------------------------

%prep
%setup -q -n %name-%version

%build
%cmake_kde4
%make

%install
rm -rf %buildroot
%{makeinstall_std} -C build
%find_lang %name --with-html

%clean
rm -rf %buildroot
