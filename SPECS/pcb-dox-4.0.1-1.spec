# RPM spec file for pcb-dox
#
# Copyright (c) 2017 Bert Timmerman <bert.timmerman@xs4all.nl>
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
Version:        4.0.1
BuildArch:      noarch
Release:        1%{?dist}
Summary:        An interactive printed circuit board editor
License:        GPLv2
Group:          Applications/Engineering
URL:            http://pcb.geda-project.org/
Source0:        https://sourceforge.net/projects/%{name}/files/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: unzip
BuildRequires: doxygen

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%package dox

Summary : Doxygen documentation for %{name} developers

%description dox
This package contains the Doxygen developer documentation of PCB,
an interactive printed circuit board editor.

%description
pcb is a CAD (computer aided design) program for the physical design
of printed circuit boards.  It has an autorouter, a trace optimizer a
design rule checker and many more features. It can create RS-274-X
(Gerber), Postscript, EPS and PNG output files.

%prep
%setup -q

%build
cd doc/doxygen
./create_pcb_dox.sh || :

%install
# install Doxygen documentation for developers by hand
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}/doxygen/
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}/doxygen/html/
cp -p doc/doxygen/*.html %{buildroot}%{_docdir}/%{name}-%{version}/doxygen/
cp -p doc/doxygen/*.png %{buildroot}%{_docdir}/%{name}-%{version}/doxygen/
cp -p doc/doxygen/*.txt %{buildroot}%{_docdir}/%{name}-%{version}/doxygen/
cp -p doc/doxygen/html/*.* %{buildroot}%{_docdir}/%{name}-%{version}/doxygen/html/

%post

%postun

%clean
rm -rf %{buildroot}

%files dox
%defattr(-,root,root)
%dir %{_docdir}/%{name}-%{version}
%doc %{_docdir}/%{name}-%{version}/doxygen/*.html
%doc %{_docdir}/%{name}-%{version}/doxygen/*.png
%doc %{_docdir}/%{name}-%{version}/doxygen/*.txt
%doc %{_docdir}/%{name}-%{version}/doxygen/html/*.*

%changelog
* Sun Aug 27 2017 bert.timmerman@xs4all.nl
- first spec file for release 4.0.1.

* Sat May 13 2017 bert.timmerman@xs4all.nl
- first spec file for release 4.0.0.
