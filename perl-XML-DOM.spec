%define upstream_name    XML-DOM
%define upstream_version 1.44

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	XML::DOM - build DOM Level 1 compliant document structures
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TJ/TJMATHER/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-XML-Parser >= 2.30
BuildRequires:	perl-XML-RegExp
BuildRequires:	perl-libwww-perl
BuildRequires:	perl-libxml-perl >= 0.07
BuildArch:	noarch
Provides:	perl-libxml-enno
Obsoletes:	perl-libxml-enno
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This is a Perl extension to XML::Parser. It adds a new 'Style' to
XML::Parser, called 'Dom', that allows XML::Parser to build an Object
Oriented datastructure with a DOM Level 1 compliant interface.
However, there is a new DOM module, XML::GDOME which is under active
development and significantly faster than XML::DOM, since it is based
on the libgdome C library.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# some old'ish utf8 stuff, nuke it (rgs)
rm -f t/dom_jp_attr.t
rm -f t/dom_jp_cdata.t
rm -f t/dom_jp_example.t
rm -f t/dom_jp_minus.t
rm -f t/dom_jp_modify.t
rm -f t/dom_jp_print.t
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%dir %{perl_vendorlib}/XML/DOM
%{perl_vendorlib}/XML/DOM.pm
%{perl_vendorlib}/XML/DOM/*.pod
%{perl_vendorlib}/XML/DOM/*.pm
%{perl_vendorlib}/XML/Handler/*
%{_mandir}/man3/*
