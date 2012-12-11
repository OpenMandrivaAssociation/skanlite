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


%changelog
* Fri Apr 27 2012 Crispin Boylan <crisb@mandriva.org> 0.8-1
+ Revision: 793964
- New release

* Wed Dec 01 2010 Funda Wang <fwang@mandriva.org> 0.7-1mdv2011.0
+ Revision: 604302
- update to new version 0.7

* Tue Nov 30 2010 Funda Wang <fwang@mandriva.org> 0.6-1mdv2011.0
+ Revision: 603282
- new version 0.6

* Sat Feb 13 2010 Funda Wang <fwang@mandriva.org> 0.4-1mdv2010.1
+ Revision: 505217
- new version 0.4

* Sat May 02 2009 Funda Wang <fwang@mandriva.org> 0.3-1mdv2010.0
+ Revision: 370591
- New version 0.3

* Sat Aug 09 2008 Funda Wang <fwang@mandriva.org> 0.2-2mdv2009.0
+ Revision: 270114
- remove old patch
- fix desktop file

* Tue Jul 29 2008 Funda Wang <fwang@mandriva.org> 0.2-1mdv2009.0
+ Revision: 252925
- New version 0.2

* Fri Jul 18 2008 Funda Wang <fwang@mandriva.org> 0.1-1mdv2009.0
+ Revision: 238143
- import skanlite

