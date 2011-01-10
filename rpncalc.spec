Name: rpncalc
Version: 1.36.8
Release: %mkrel 1
Summary: An RPN calculator similar to the HP28S
URL: http://packages.debian.org/unstable/source/rpncalc
Source: %{name}_%{version}.tar.gz
Patch0: %{name}-1.36.8-make-install.patch
Patch1: %{name}-1.36.8-bison.patch
Group: Sciences/Mathematics
License: GPL
BuildRequires: bison
BuildRequires: flex
BuildRequires: libncurses-devel
BuildRequires: libreadline-devel
BuildRequires: ed
BuildRoot: %{_tmppath}/%{name}-%{version}-root

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
%lang(de) %{_mandir}/de/man1/rpncalc.1.gz
%lang(es) %{_mandir}/es/man1/rpncalc.1.gz
