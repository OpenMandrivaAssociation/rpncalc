Name: rpncalc
Version: 1.36.8
Release: 3
Summary: An RPN calculator similar to the HP28S
URL: https://packages.debian.org/unstable/source/rpncalc
Source: %{name}_%{version}.tar.gz
Patch0: %{name}-1.36.8-make-install.patch
Patch1: %{name}-1.36.8-bison.patch
Group: Sciences/Mathematics
License: GPL
BuildRequires: bison
BuildRequires: flex
BuildRequires: ncurses-devel
BuildRequires: readline-devel
BuildRequires: ed

%description
rpncalc is a calculator similar to dc(1), but it uses the readline library
and shows the stack visually.

%prep
%setup -q -n %{name}
%patch0 -p1 -b .make-install
%patch1 -p1 -b .bison

%build
%make

%install
%make install DESTDIR=%{buildroot}
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README COPYING debian/changelog
%{_bindir}/rpncalc
%{_mandir}/man1/rpncalc.1*
%lang(de) %{_mandir}/de/man1/rpncalc.1*
%lang(es) %{_mandir}/es/man1/rpncalc.1*


%changelog
* Tue Jan 18 2011 Claudio Matsuoka <claudio@mandriva.com> 1.36.8-1mdv2011.0
+ Revision: 631394
- new upstream release
  * get rid of autoconf machinery
  * add different translations
  * add binary mode input/output
  * fix memory allocation error (Debian bug #439001)
- force bison as parser generator, byacc seems to be broken (bug #62154)

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.35-6mdv2010.0
+ Revision: 442762
- rebuild

* Tue Mar 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.35-5mdv2009.1
+ Revision: 347891
- rebuild for latest readline

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 1.35-4mdv2009.0
+ Revision: 260340
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 1.35-3mdv2009.0
+ Revision: 251536
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.35-1mdv2008.1
+ Revision: 126750
- kill re-definition of %%buildroot on Pixel's request
- import rpncalc


* Thu Feb 02 2006 Lenny Cartier <lenny@mandriva.com> 1.35-1mdk
- 1.35

* Wed May 18 2005 Claudio Matsuoka <claudio@mandriva.com> 1.34-1mdk
- package creation
