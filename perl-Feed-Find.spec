#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Feed
%define	pnam	Find
Summary:	Feed::Find - Syndication feed auto-discovery
Summary(pl.UTF-8):	Feed::Find - automatyczne wykrywanie feedów zespolonych
Name:		perl-Feed-Find
Version:	0.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/B/BT/BTROTT/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	be4537f652d41243cbf98f5e937d16f3
URL:		http://search.cpan.org/dist/Feed-Find/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-ErrorHandler
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-URI
BuildRequires:	perl-libwww
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Feed::Find implements feed auto-discovery for finding syndication feeds,
given a URI. It (currently) passes all of the auto-discovery tests at
<http://diveintomark.org/tests/client/autodiscovery/>.

%description -l pl.UTF-8
Feed::Find implementuje automatyczne wykrywanie feedów do znajdowania
feedów zespolonych dla danego URI. (Aktualnie) przechodzi wszystkie
testy automatycznego wykrywania pod
<http://diveintomark.org/tests/client/autodiscovery/>.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Feed
%{_mandir}/man3/*
