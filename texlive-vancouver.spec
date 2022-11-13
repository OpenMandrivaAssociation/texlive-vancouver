Name:		texlive-vancouver
Version:	59192
Release:	1
Summary:	Bibliographic style file for Biomedical Journals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/vancouver
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vancouver.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vancouver.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This BibTeX style file is generated with the docstrip utility
and modified manually to meet the Uniform Requirements for
Manuscripts Submitted to Biomedical Journals as published in N
Engl J Med 1997;336:309-315 (also known as the Vancouver
style). The complete set of requirements may be viewed on the
ICMJE web site.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/vancouver
%doc %{_texmfdistdir}/doc/bibtex/vancouver

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc %{buildroot}%{_texmfdistdir}
