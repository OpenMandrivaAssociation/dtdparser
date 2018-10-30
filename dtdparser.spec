%{?_javapackages_macros:%_javapackages_macros}
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

Name:           dtdparser
Version:        1.21
Release:        15.3
Summary:        A Java DTD Parser
Group:		Development/Java

# The code has no license attribution.
# There is a LICENSE.INFO file, but it does not specify versions.
# The only versioning is in the ASL_LICENSE file, which has been edited by the upstream.
License:        LGPLv2+ or ASL 1.1
URL:            http://wutka.com/%{name}.html
BuildArch:      noarch

Source0:        http://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{version}.tgz
Source1:        http://repo1.maven.org/maven2/com/wutka/%{name}/%{version}/%{name}-%{version}.pom

# Without removing these comments, build fails
Patch0:         %{name}-unmappable-chars-in-comments.patch

BuildRequires:  ant
BuildRequires:  java-devel
BuildRequires:  jpackage-utils

Requires:       java-headless
Requires:       jpackage-utils

%description
DTD parsers for Java seem to be pretty scarce. That's probably because
DTD isn't valid XML. At some point, if/when XML Schema becomes widely
accepted, no one will need DTD parsers anymore. Until then, you can
use this library to parse a DTD.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
find -name \*.jar -delete -o -name \*.class -delete

echo com.wutka.dtd > doc/package-list

sed -i "s,59 Temple Place,51 Franklin Street,;s,Suite 330,Fifth Floor,;s,02111-1307,02110-1301," LICENSE

%patch0

%build
ant build createdoc

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 dist/%{name}120.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr doc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# POM
install -d -m 0755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files -f .mfiles
%doc CHANGES LICENSE README ASL_LICENSE


%files javadoc
%doc %{_javadocdir}/*
%doc LICENSE ASL_LICENSE

%changelog
* Tue Jun 10 2014 Gerard Ryan <galileo@fedoraproject.org> - 1.21-15
- Generate maven metadata for dtdparser

* Sun Jun 08 2014 Gerard Ryan <galileo@fedoraproject.org> - 1.21-14
- Remove old maven depmap stuff

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 02 2014 Gerard Ryan <galileo@fedoraproject.org> - 1.21-12
- RHBZ-1068030: Switch to java-headless requires

* Fri Aug 23 2013 Gerard Ryan <galileo@fedoraproject.org> - 1.21-11
- Bump release

* Mon Jul 29 2013 Gerard Ryan <galileo@fedoraproject.org> - 1.21-10
- RHBZ-989265: Fix problems found in review request.

* Sat Jul 27 2013 Gerard Ryan <galileo@fedoraproject.org> - 1.21-9
- Unkill and clean up package.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.21-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:1.21-5
- drop repotag
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0:1.21-4jpp.2
- Autorebuild for GCC 4.3

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



