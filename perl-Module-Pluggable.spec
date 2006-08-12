#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Module
%define		pnam	Pluggable
Summary:	Automatically give your module the ability to have plugins
Summary(pl):	Automatyczne umo�liwianie modu�om posiadania wtyczek
:e Name:		perl-Module-Pluggable
Version:	3.1
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4ca7144b4a0da45bed0ab986c187f328
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
Ten modu� dostarcza prosty, ale rozszerzalny spos�b posiadania
"wtyczek" dla w�asnego modu�u. Oczywi�cie nie jest to pe�ne i ko�cowe
rozwi�zanie, ale autorowi dzia�a.

Zasadniczo wszystko co robi ten modu� to wyeksportowanie metody
przeszukuj�cej �cie�k� pod k�tem plik�w .pm i zamieniaj�cej je na
nazwy klas. Opcjonalnie mo�e dziedziczy� te klasy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Module/Pluggable.pm
# TODO: add Pluggable dir to perl-base
%{perl_vendorlib}/Module/Pluggable/*
%{perl_vendorlib}/Devel/InnerPackage.pm
%{_mandir}/man3/*
