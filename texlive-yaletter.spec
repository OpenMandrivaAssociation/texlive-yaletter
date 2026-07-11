%global tl_name yaletter
%global tl_revision 42830

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Extremely flexible macros for letters, envelopes, and label sheets
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/yaletter
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/yaletter.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/yaletter.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/yaletter.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The yaletter class provides extremely configurable macros for
typesetting letters in any conceivable style. It provides facilities for
maintaining easily-accessible databases of letterheads and addresses for
repeat use. It further provides easy macros for envelopes and for label
sheets. Finally, it provides some nice defaults for a few of the more
common styles and sizes.

