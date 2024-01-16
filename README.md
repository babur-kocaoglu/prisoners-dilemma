\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage[ruled,vlined]{algorithm2e}
\usepackage{graphicx}
\usepackage{amsmath,amsthm,amssymb,amsfonts}
\usepackage{graphicx}
\usepackage{minted}
\usepackage{placeins}
\newminted{python}{%
    % options to customize output of pythoncode
    % see section 5.3 Available options starting at page 16
}

\title{Computational Optimization of The Prisoner's Dilemma}
\author{Babur Kocaoglu}
\date{April 30, 2021}

\begin{document}

\maketitle

\section{Introduction}


We begin with the simplified prisoner's dilemma.  This is defined by a matrix \(A\) of values.  Example:
\[A=\begin{bmatrix}
4 & 0 & 5\\
4 & 4 & 3\\
2 & 6 & 2\end{bmatrix}\]
In the classical prisoner's dilemma, we must pick a row and our opponent must pick a column.  Here, though, we intend to play perfectly and selfishly: Our opponent knows what we will do and will do what's best for him.  We will do what's best for us (which, in this simplified case, is what's worst for him). \\
\\
In other words, we pick a row such that, when our opponent picks a column, he is forced to pick his own worst possible outcome.  However, since he knows what we're going to do, picking a single row outright may be sub-ideal: as such, we will pick row \(i\) with a probability \(p_i\), and our opponent must play accordingly.\\
\\
Knowing the \(p_i\)'s, our opponent can generate a value vector by simply taking the row vector \(p=[p_1,p_2,...,p_m]\) and multiplying it by \(A\), taking the weighted mean of the rows.  Then, he can pick the highest value, thereby giving himself the highest possible (average) payout.  This means that while our actions are probabilistic, his action will be deterministic: whatever distribution we present, we can determine what our opponent will do.  This lets us create our \\optimization equation:
\[\arg_p\min (\max_i (pA)_i)\]
with constraints 
\[||p||_1=1\]
\[p_i\geq 0\;\;\forall i\]
\newpage
Returning to our example matrix, \(A\), this becomes
\[\arg_p\min (\max ((pA)_1,(pA)_2,(pA)_3))=\arg_p\min (\max (4p_1+4p_2+2p_3,4p_2+6p_3,5p_1+3p_2+2p_3))\]
and noting that \(p_3=1-p_1-p_2\), it simplifies to
\[\arg_p\min (\max (2p_1+2p_2+2,-6p_1-2p_2+6,3p_1+p_2+2))\]
Now, fix \(\max (2p_1+2p_2+2,-6p_1-2p_2+6,3p_1+p_2+2)=C\), and solve for the system of equations
\[\begin{bmatrix}
2p_1&+2p_2&+2&=C\\
-6p_1&-2p_2&+6&=C\\
3p_1&+p_2&+2&=C
\end{bmatrix}\]
\[\begin{bmatrix}
0&+4p_2&+12&=4C\\
2p_1&+2p_2&+2&=C\\
3p_1&+p_2&+2&=C
\end{bmatrix}\]
\[\begin{bmatrix}
0&+4p_2&+12&=4C\\
6p_1&+6p_2&+6&=3C\\
6p_1&+2p_2&+4&=2C
\end{bmatrix}\]
\[\begin{bmatrix}
0&+4p_2&+12&=4C\\
0&+4p_2&+2&=C\\
6p_1&+2p_2&+4&=2C
\end{bmatrix}\]
\[\begin{bmatrix}
0&+4p_2&+12&=4C\\
0&+4p_2&+2&=C\\
6p_1&-6p_2&0&=0
\end{bmatrix}\]
\[\begin{bmatrix}
0&0&+10&=3C\\
0&+4p_2&+2&=C\\
p_1&-p_2&0&=0
\end{bmatrix}\]
\[\begin{bmatrix}
0&0&+\frac{10}{3}&=C\\
0&+4p_2&+2-\frac{10}{3}&=0\\
p_1&-p_2&0&=0
\end{bmatrix}\]
\[\begin{bmatrix}
0&0&+\frac{10}{3}&=C\\
0&+4p_2&-\frac{4}{3}&=0\\
p_1&-p_2&0&=0
\end{bmatrix}\]
\[\begin{bmatrix}
0&0&+\frac{10}{3}&=C\\
0&+p_2&-\frac{1}{3}&=0\\
p_1&-p_2&0&=0
\end{bmatrix}\]
which gives us our answer: \(p_1=p_2=p_3=\frac{1}{3}\) and \(C=\frac{10}{3}\).
\[p=\begin{bmatrix}\frac{1}{3}&\frac{1}{3}&\frac{1}{3}\end{bmatrix}\]
\\
\\
This process, however, is not always so simple. Consider another example.
