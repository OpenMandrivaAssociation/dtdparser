# Copyright (c) 2000-2007, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%define _with_gcj_support 1

%define gcj_support %{?_with_gcj_support:1}%{!?_with_gcj_support:%{?_without_gcj_support:0}%{!?_without_gcj_support:%{?_gcj_support:%{_gcj_support}}%{!?_gcj_support:0}}}

%define section         free

Name:           dtdparser
Version:        1.21
Release:        3.2.14
Epoch:          0
Summary:        A Java DTD Parser
License:        LGPL
Source0:        http://wutka.com/download/%{name}-%{version}.tgz
URL:            http://wutka.com/dtdparser.html
BuildRequires:  ant
BuildRequires:  locales-en
BuildRequires:  java-rpmbuild
Requires:       java
Requires:       jpackage-utils >= 0:1.6
Requires(postun): jpackage-utils >= 0:1.6 
Group:          Development/Java
%if ! %{gcj_support}
BuildArch:      noarch
%endif

%if %{gcj_support}
BuildRequires:                java-gcj-compat-devel
%endif

%description
DTD parsers for Java seem to be pretty scarce. That's probably because
DTD isn't valid XML. At some point, if/when XML Schema becomes widely
accepted, no one will need DTD parsers anymore. Until then, you can
use this library to parse a DTD.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils >= 0:1.6
Requires(postun): jpackage-utils >= 0:1.6 

%description javadoc
Javadoc for %{name}.

# -----------------------------------------------------------------------------

%prep
%setup -q
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;

# -----------------------------------------------------------------------------

%build
export LC_ALL=ISO-8859-1
%{ant} build createdoc

# -----------------------------------------------------------------------------

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 dist/%{name}120.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr doc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# -----------------------------------------------------------------------------

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

# -----------------------------------------------------------------------------

%if %{gcj_support}
%post
%{update_gcjdb}

%postun
%{clean_gcjdb}
%endif

%files
%defattr(0644,root,root,0755)
%doc CHANGES LICENSE README
%{_javadir}/*

%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/dtdparser-1.21.jar.*
%endif

%files javadoc
%defattr(0644,root,root,0755)
%doc %{_javadocdir}/*

# -----------------------------------------------------------------------------


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0:1.21-3.2.7mdv2011.0
+ Revision: 663891
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0:1.21-3.2.6mdv2011.0
+ Revision: 604831
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0:1.21-3.2.5mdv2010.1
+ Revision: 522539
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0:1.21-3.2.4mdv2010.0
+ Revision: 413411
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0:1.21-3.2.3mdv2009.0
+ Revision: 140722
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Dec 16 2007 Anssi Hannula <anssi@mandriva.org> 0:1.21-3.2.3mdv2008.1
+ Revision: 120807
- buildrequires java-rpmbuild

* Sat Sep 15 2007 Anssi Hannula <anssi@mandriva.org> 0:1.21-3.2.2mdv2008.0
+ Revision: 87342
- rebuild to filter out autorequires of GCJ AOT objects
- remove unnecessary Requires(post) on java-gcj-compat

* Wed Jul 04 2007 David Walluck <walluck@mandriva.org> 0:1.21-3.2.1mdv2008.0
+ Revision: 48029
- Import dtdparser



* Tue Feb 13 2007 Tania Bento <tbento@redhat.com> - 0:1.21-3jpp.1.fc7
- Fixed the %%Release tag.
- Fixed the %%BuildRoot tag.
- Add gcj support

* Thu Apr 27 2006 Fernando Nasser <fnasser@redhat.com> - 0:1.21-3jpp
- First JPP 1.7 build

* Fri Aug 20 2004 Ralph Apel <r.apel at r-apel.de> 0:1.21-2jpp
- Build with ant-1.6.2

* Fri Apr 11 2003 David Walluck <david@anti-microsoft.org> 0:1.21-1jpp
- 1.21

* Tue Mar  4 2003 Ville Skyttä <ville.skytta at iki.fi> - 1.20-1jpp
- Update to 1.20.
- Fix Group, Distribution and Vendor tags.
- Use sed instead of bash 2 extension for symlink creation during build.
- Use build.xml from upstream tarball.

* Mon Jan 21 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.15-3jpp
- versioned dir for javadoc
- no dependencies for javadoc package
- section macro

* Wed Dec 5 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.15-2jpp
- javadoc into javadoc package

* Wed Nov 21 2001 Christian Zoffoli <czoffoli@littlepenguin.org> 1.15-1jpp
- removed packager tag
- new jpp extension
- 1.15

* Sat Oct 6 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.13-4jpp
- used original tarball

* Sun Sep 30 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.13-3jpp
- more macros

* Fri Sep 28 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.13-2jpp
- first unified JPackage release
- spec cleanup
- corrected buildfile
- s/jPackage/JPackage

* Sat Jun 23 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.13-1jpp
- first Mandrake release
