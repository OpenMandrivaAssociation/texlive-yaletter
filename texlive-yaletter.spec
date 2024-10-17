Name:		texlive-yaletter
Version:	42830
Release:	2
Summary:	Extremely flexible macros for letters, envelopes, and label sheets
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/yaletter
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yaletter.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yaletter.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yaletter.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The yaletter class provides extremely configurable macros for
typesetting letters in any conceivable style. It provides
facilities for maintaining easily-accessible databases of
letterheads and addresses for repeat use. It further provides
easy macros for envelopes and for label sheets. Finally, it
provides some nice defaults for a few of the more common styles
and sizes.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/yaletter
%{_texmfdistdir}/tex/latex/yaletter
%doc %{_texmfdistdir}/doc/latex/yaletter

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
