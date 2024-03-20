# Line Integral
$$
\begin{aligned}
ds&=||\vec{r}'(t)||dt \\
\int_C f(x,y,z)ds&=\int_a^bf(g(t),h(t),k(t))|\vec{v}(t)|dt
\end{aligned}
$$
# Thin wire
## Mass
$$\int_C \delta ds$$
## First Moments
$$\begin{aligned}M_{yz} &= \int_C x \delta ds \\ M_{xz} &= \int_C y \delta ds \\ M_{xy}&= \int_C z \delta ds \end{aligned}$$
## Moment of inertia
$$
\begin{aligned} I_x&=\int_C(y^2+z^2) \delta ds \\ I_y&=\int_C(x^2+z^2) \delta ds \\ I_z&=\int_C(x^2+y^2) \delta ds \\ 
r(x,y,z) &= \text{distance from point $(x,y,z)$ to line $L$} \\
I_L &= \int_C r^2 \delta ds
\end{aligned}
$$
# Line Integral of Vector Field
$\vec{F} \text{ along } C:$
$$
\begin{aligned} 
\int_C \vec{F} \cdot \vec{T} ds &=\int_C \vec{F} \cdot \frac{d\vec{r}}{ds} ds\\ 
&=\int_C \vec{F} \cdot d \vec{r}\\ 
&=\int_a^b \vec{F}(\vec{r}(t)) \cdot \frac{d \vec{r}}{dt}dt
\end{aligned}
$$
$$
\begin{aligned}
\int_C Mdx+Ndy+Pdz &=\int_C M(x,y,z)dx+\int_C N(x,y,z)dy+\int_C P(x,y,z)dz \\ 
\text{Where, }\int_C M(x,y,z)dx &=\int_C M(g(t),h(t),k(t))g'(t)dt
\end{aligned}
$$
## Applications
$$
\begin{aligned}
\text{Work}&=\int_C \vec{F} \cdot \vec{T}\ ds \\
\text{Flow}&=\int_C \vec{F} \cdot \vec{T} \ ds=\int_CMdx+Ndy \\
\text{Flux}&=\int_C \vec{F} \cdot \vec{n} \ ds=\oint_CMdy-Ndx
\end{aligned}
$$
# Conservative Fields
Fields are conservative if $\displaystyle \int_C \vec{F} \cdot d \vec{r}$ is path independent.
$\vec{F}=\nabla f$ then $f$ is the potential function for $\vec{F}$. So $\vec{F}$ can be represented as such: 
$$\vec{F} = M(x,y,z)\mathbf{i} +N(x,y,z)\mathbf{j}+P(x,y,z)\mathbf{k}$$
$\vec{F}$ must have a potential function to be conservative. Also, $\vec{F}$ conservative are if and only if:
$$
\frac{\partial{P}}{\partial{y}}=\frac{\partial{N}}{\partial{z}}, \quad
\frac{\partial{M}}{\partial{z}}=\frac{\partial{P}}{\partial{x}}, \quad
\frac{\partial{N}}{\partial{x}}=\frac{\partial{M}}{\partial{y}}
$$
For a conservative vector field, $\displaystyle \vec{F}, \int_C \vec{F} \cdot d \vec{r}=f(B)-f(A)$
