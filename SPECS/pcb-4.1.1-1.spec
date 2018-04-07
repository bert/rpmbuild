# RPM spec file for pcb
#
# Copyright (c) 2017, 2018 Bert Timmerman <bert.timmerman@xs4all.nl>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


Name:           pcb
Version:        4.1.1
Release:        1%{?dist}
Summary:        An interactive printed circuit board editor
License:        GPLv2
Group:          Applications/Engineering
URL:            http://pcb.geda-project.org/
Source0:        https://sourceforge.net/projects/%{name}/files/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz

#BuildRequires: autoconf >= 2.69
BuildRequires: autoconf
BuildRequires: ImageMagick
BuildRequires: bison
#BuildRequires: gettext >= 0.19.3
BuildRequires: gettext
BuildRequires: dbus-devel
BuildRequires: flex
BuildRequires: byacc
BuildRequires: gawk
BuildRequires: freeglut-devel
#BuildRequires: freetype2-devel
BuildRequires: gcc-c++
BuildRequires: gd-devel
BuildRequires: gtk2-devel
BuildRequires: gtkglext-devel
BuildRequires: intltool >= 0.35.0
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: perl-XML-Parser
BuildRequires: texinfo >= 4.6
BuildRequires: texinfo-tex
BuildRequires: m4
BuildRequires: tk
BuildRequires: unzip
BuildRequires: desktop-file-utils
BuildRequires: gerbv
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(gdlib)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(gtkglext-1.0)

Requires(post): shared-mime-info

Requires(postun): shared-mime-info

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
pcb is a CAD (computer aided design) program for the physical design
of printed circuit boards.
It has an autorouter, Blind and Buried Vias, a trace optimizer, a design
rule checker and many more features.
It can create RS-274-X (Gerber), G-code, IPC-D-356, Nelma, GSvit,
Postscript, EPS and PNG output files.

%prep
%setup -q

%build
# pcb does not like the -D_FORTIFY_SOURCE=2 option, remove it.
export CFLAGS=$(echo %{optflags} | sed "s,-D_FORTIFY_SOURCE=2,,g")
%configure  \
            --docdir=%{_docdir}/%{name} \
            --disable-rpath \
            --enable-dbus \
            --disable-update-desktop-database \
            --disable-update-mime-database \
            --enable-gl \
            --enable-toporouter \
            --enable-toporouter-output

make %{?_smp_mflags}

%install
%make_install

# acpcircuits support
# http://www.apcircuits.com/resources/links/pcb_unix.html
unzip tools/apctools.zip
install -p -m 755 apc*.pl  %{buildroot}%{_datadir}/%{name}/tools

# fix W: non-executable-script
chmod 755 %{buildroot}%{_datadir}/%{name}/tools/{Merge*,PCB2HPGL,pcbdiff,tgo2pcb.tcl}

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}/
install -Dm 644 {AUTHORS,ChangeLog,COPYING,INSTALL,NEWS,README} %{buildroot}%{_docdir}/%{name}-%{version}/
install -Dm 644 doc/pcb.info %{buildroot}%{_infodir}/%{name}.info
install -Dm 644 doc/pcb.pdf %{buildroot}%{_docdir}/%{name}-%{version}/
install -Dm 644 doc/pcb.html %{buildroot}%{_docdir}/%{name}-%{version}/
install -Dm 644 doc/debumpify*.png %{buildroot}%{_docdir}/%{name}-%{version}/
install -Dm 644 doc/gcode*.png %{buildroot}%{_docdir}/%{name}-%{version}/
install -Dm 644 doc/miter*.png %{buildroot}%{_docdir}/%{name}-%{version}/
install -Dm 644 doc/orthopull*.png %{buildroot}%{_docdir}/%{name}-%{version}/
install -Dm 644 doc/pad.png %{buildroot}%{_docdir}/%{name}-%{version}/
install -Dm 644 doc/puller.png %{buildroot}%{_docdir}/%{name}-%{version}/
install -Dm 644 doc/td_ex1.png %{buildroot}%{_docdir}/%{name}-%{version}/
install -Dm 644 doc/thermal.png %{buildroot}%{_docdir}/%{name}-%{version}/
install -Dm 644 doc/unjaggy*.png %{buildroot}%{_docdir}/%{name}-%{version}/
install -Dm 644 doc/vianudge*.png %{buildroot}%{_docdir}/%{name}-%{version}/
install -Dm 644 doc/viatrim*.png %{buildroot}%{_docdir}/%{name}-%{version}/
install -Dm 644 README_FILES/Tools %{buildroot}%{_docdir}/%{name}-%{version}/README_Tools

# install files for Doxygen documentation for developers by hand
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}/doxygen/
install -Dm 644 doc/doxygen/pcb.dox %{buildroot}%{_docdir}/%{name}-%{version}/doxygen/
install -Dm 755 doc/doxygen/create_pcb_dox.sh %{buildroot}%{_docdir}/%{name}-%{version}/doxygen/
install -Dm 644 doc/doxygen/*.html %{buildroot}%{_docdir}/%{name}-%{version}/doxygen/
install -Dm 644 doc/doxygen/*.png %{buildroot}%{_docdir}/%{name}-%{version}/doxygen/
install -Dm 644 doc/doxygen/*.txt %{buildroot}%{_docdir}/%{name}-%{version}/doxygen/

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}/examples/
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}/examples/libraries/
install -Dm 644 example/LED*.* %{buildroot}%{_docdir}/%{name}-%{version}/examples/
install -Dm 644 example/libraries/example.* %{buildroot}%{_docdir}/%{name}-%{version}/examples/libraries/

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}/tutorial/
install -Dm 644 tutorial/tut1.pcb %{buildroot}%{_docdir}/%{name}-%{version}/tutorial/

### Clean up ###

# remove acptools.zip and pcb2ncap.tgz
rm -f %{buildroot}%{_datadir}/%{name}/tools/apctools.zip
rm -f %{buildroot}%{_datadir}/%{name}/tools/pcb2ncap.tgz

# remove static library, header and source file
rm -f %{buildroot}%{_libdir}/libgts.a \
      %{buildroot}%{_includedir}/gts.h \
      %{buildroot}%{_datadir}/%{name}/tools/gerbertotk.c

# remove duplicates
%{__rm} -f %{buildroot}%{_bindir}/Merge*

# remove conflicting dir file
%{__rm} -f %{buildroot}/usr/share/info/dir

# remove conflicting doc subdirectory
%{__rm} -rf %{buildroot}/usr/share/doc/pcb/

# locale's
%find_lang %{name}

%post
/usr/bin/update-mime-database %{_datadir}/mime &> /dev/null || :
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%postun
/usr/bin/update-mime-database %{_datadir}/mime &> /dev/null || :
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%dir %{_docdir}/%{name}-%{version}
%doc %{_docdir}/%{name}-%{version}/AUTHORS
%doc %{_docdir}/%{name}-%{version}/COPYING
%doc %{_docdir}/%{name}-%{version}/ChangeLog
%doc %{_docdir}/%{name}-%{version}/INSTALL
%doc %{_docdir}/%{name}-%{version}/NEWS
%doc %{_docdir}/%{name}-%{version}/README
%doc %{_docdir}/%{name}-%{version}/README_Tools
%doc %{_docdir}/%{name}-%{version}/*.html
%doc %{_docdir}/%{name}-%{version}/*.pdf
%doc %{_docdir}/%{name}-%{version}/*.png
%doc %{_docdir}/%{name}-%{version}/doxygen/create_pcb_dox.sh
%doc %{_docdir}/%{name}-%{version}/doxygen/pcb.dox
%doc %{_docdir}/%{name}-%{version}/doxygen/*.html
%doc %{_docdir}/%{name}-%{version}/doxygen/*.png
%doc %{_docdir}/%{name}-%{version}/doxygen/*.txt
%doc %{_docdir}/%{name}-%{version}/examples/LED*.*
%doc %{_docdir}/%{name}-%{version}/examples/libraries/example.*
%doc %{_docdir}/%{name}-%{version}/tutorial/tut1.pcb
%{_bindir}/%{name}
%{_datadir}/gEDA/scheme/*
%{_datadir}/%{name}/
%{_iconsdir}/hicolor/*/mimetypes/application-x-*
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_datadir}/applications/pcb.desktop
%{_datadir}/mime/packages/*
%{_mandir}/man1/%{name}*
%{_infodir}/%{name}.info*.gz
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/pcb.appdata.xml

%changelog
* Sat Apr 7 2018 bert.timmerman@xs4all.nl
- first spec file for release 4.1.1.

* Sun Jan 28 2018 bert.timmerman@xs4all.nl
- first spec file for release 4.1.0.

* Fri Sep 1 2017 bert.timmerman@xs4all.nl
- first spec file for release 4.0.2.

* Sun Aug 27 2017 bert.timmerman@xs4all.nl
- first spec file for release 4.0.1.

* Fri May 19 2017 bert.timmerman@xs4all.nl
- first spec file for release 4.0.0.

