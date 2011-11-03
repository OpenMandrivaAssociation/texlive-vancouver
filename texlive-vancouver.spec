# revision 15878
# category Package
# catalog-ctan /biblio/bibtex/contrib/vancouver
# catalog-date 2007-03-13 09:06:46 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-vancouver
Version:	20070313
Release:	1
Summary:	Bibliographic style file for Biomedical Journals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/vancouver
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vancouver.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vancouver.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This BibTeX style file is generated with the docstrip utility
and modified manually to meet the Uniform Requirements for
Manuscripts Submitted to Biomedical Journals as published in N
Engl J Med 1997;336:309-315 (also known as the Vancouver
style). The complete set of requirements may be viewed on the
ICMJE web site.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bib/vancouver/vancouver.bib
%{_texmfdistdir}/bibtex/bst/vancouver/vancouver.bst
%doc %{_texmfdistdir}/doc/bibtex/vancouver/README
%doc %{_texmfdistdir}/doc/bibtex/vancouver/vancouver.pdf
%doc %{_texmfdistdir}/doc/bibtex/vancouver/vancouver.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
