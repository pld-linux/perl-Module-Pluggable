#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Module
%define		pnam	Pluggable
Summary:	Automatically give your module the ability to have plugins
Summary(pl):	Automatyczne umo¿liwianie modu³om posiadania wtyczek
Name:		perl-Module-Pluggable
Version:	2.9
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b839425a11adf0dd3845cd1b7d22032c
BuildRequires:	perl-Module-Build >= 0.02
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a simple but, hopefully, extensible way of having 'plugins'
for your module. Obviously this isn't going to be the be all and end
all of solutions but it works for me.

Essentially all it does is export a method into your namespace that
looks through a search path for .pm files and turn those into class
names. Optionally it instantiates those classes for you.

%description -l pl
Ten modu³ dostarcza prosty, ale rozszerzalny sposób posiadania
"wtyczek" dla w³asnego modu³u. Oczywi¶cie nie jest to pe³ne i koñcowe
rozwi±zanie, ale autorowi dzia³a.

Zasadniczo wszystko co robi ten modu³ to wyeksportowanie metody
przeszukuj±cej ¶cie¿kê pod k±tem plików .pm i zamieniaj±cej je na
nazwy klas. Opcjonalnie mo¿e dziedziczyæ te klasy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{perl_vendorlib}/%{pdir},%{_mandir}/man3}

install blib/lib/Module/Pluggable.pm $RPM_BUILD_ROOT%{perl_vendorlib}/%{pdir}
install blib/man3/*pm $RPM_BUILD_ROOT%{_mandir}/man3

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Module/Pluggable.pm
%{_mandir}/man3/*
