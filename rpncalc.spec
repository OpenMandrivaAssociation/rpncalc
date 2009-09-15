Name: rpncalc
Version: 1.35
Release: %mkrel 6
Summary: An RPN calculator similar to the HP28S
URL: http://packages.debian.org/unstable/source/rpncalc
Source: %{name}_%{version}.tar.bz2
Group: Sciences/Mathematics
License: GPL
BuildRequires: bison
BuildRequires: flex
BuildRequires: libncurses-devel
BuildRequires: libreadline-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
rpncalc is a calculator similar to dc(1), but it uses the readline library
and shows the stack visually.

%prep
%setup -q

%build
%configure
make

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_libdir}

install -s -m 755 rpncalc %{buildroot}%{_bindir}/rpncalc
install -m 644 rpncalc.1 %{buildroot}%{_mandir}/man1/rpncalc.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING debian/changelog
%{_bindir}/rpncalc
%{_mandir}/man1/rpncalc.1*

