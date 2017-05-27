%define		packname	widgetTools

Summary:	Bioconductor tools to support tcltk widgets
Name:		R-%{packname}
Version:	1.40.0
Release:	2
License:	LGPL v2+
Group:		X11/Applications
Source0:	http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	bf2c5ccdc89b904f430ee2dc2c1b29b1
URL:		http://bioconductor.org/packages/release/bioc/html/widgetTools.html
BuildRequires:	R
BuildRequires:	tcl-devel
BuildRequires:	texlive-latex
BuildRequires:	tk-devel
Requires:	R
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains tools to support the construction of tcltk
widgets.

This library is part of the bioconductor (bioconductor.org) project

%prep
%setup -c -q -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

R CMD INSTALL %{packname} -l $RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%{_libdir}/R/library/%{packname}
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
