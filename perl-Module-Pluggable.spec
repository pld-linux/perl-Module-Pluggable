#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Module
%define		pnam	Pluggable
Summary:	Automatically give your module the ability to have plugins
Summary(pl.UTF-8):	Automatyczne umożliwianie modułom posiadania wtyczek
Name:		perl-Module-Pluggable
Version:	5.1
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Module/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1b71ed7a67ad8c048d1499540bc892ba
URL:		http://search.cpan.org/dist/Module-Pluggable/
BuildRequires:	perl-Class-Inspector
BuildRequires:	perl-Module-Build >= 0.38
%{?with_tests:BuildRequires:	perl-Test-Simple >= 0.62}
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-dirs >= 1.0-5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a simple but, hopefully, extensible way of having 'plugins'
for your module. Obviously this isn't going to be the be all and end
all of solutions but it works for me.

Essentially all it does is export a method into your namespace that
looks through a search path for .pm files and turn those into class
names. Optionally it instantiates those classes for you.

%description -l pl.UTF-8
Ten moduł dostarcza prosty, ale rozszerzalny sposób posiadania
"wtyczek" dla własnego modułu. Oczywiście nie jest to pełne i końcowe
rozwiązanie, ale autorowi działa.

Zasadniczo wszystko co robi ten moduł to wyeksportowanie metody
przeszukującej ścieżkę pod kątem plików .pm i zamieniającej je na
nazwy klas. Opcjonalnie może dziedziczyć te klasy.

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
%doc Changes
%{perl_vendorlib}/Devel/InnerPackage.pm
%{perl_vendorlib}/Module/Pluggable.pm
%dir %{perl_vendorlib}/Module
%dir %{perl_vendorlib}/Module/Pluggable
%{perl_vendorlib}/Module/Pluggable/Object.pm
%{_mandir}/man3/Devel::InnerPackage.3pm*
%{_mandir}/man3/Module::Pluggable*.3pm*
