Module 4 Formulas
$$\text{Line Integral:}$$
$$ds=||\vec{r}'(t)||dt$$
$$\int_C f(x,y,z)ds=\int_a^bf(g(t),h(t),k(t))|\vec{v}(t)|dt$$
$$\text{Mass (Thin wire)}= \int_C \delta ds$$
$$\text{First Moments (Thin wire):}$$
$$M_{yz}= \int_C x \delta ds$$		$$M_{xz}= \int_C y \delta ds$$		$$M_{xy}= \int_C z \delta ds$$
$$\text{Moment of inertia (Thin wire):}$$
$$I_x=\int_C(y^2+z^2) \delta ds$$		$$I_y=\int_C(x^2+z^2) \delta ds$$		$$I_z=\int_C(x^2+y^2) \delta ds$$	$$I_L=\int_C r^2 \delta ds \text{ where r(x,y,z) = distance from point (x,y,z) to line L}$$
$$\text{Line Integral of vector field } \vec{F} \text{ along }C:$$
$$\int_C \vec{F} \cdot \vec{T} ds=\int_C \vec{F} \cdot \frac{d\vec{r}}{ds} ds=\int_C \vec{F} \cdot d \vec{r}=\int_a^b \vec{F}(\vec{r}(t)) \cdot \frac{d \vec{r}}{dt}dt$$
$$\int_C Mdx+Ndy+Pdz=\int_C M(x,y,z)dx+\int_C N(x,y,z)dy+\int_C P(x,y,z)dz$$
$$\text{Where }\int_C M(x,y,z)dx=\int_C M(g(t),h(t),k(t))g'(t)dt$$
	$$\text{Work}=\int_C \vec{F} \cdot \vec{T}ds$$
	$$\text{Flow}=\int_C \vec{F} \cdot \vec{T}ds=\int_CMdx+Ndy$$
	$$\text{Flux}=\int_C \vec{F} \cdot \vec{T}ds=\oint_CMdy-Ndx$$
$$\text{Conservative Fields: }$$
$$\text{Fields are conservative if } \int_C \vec{F} \cdot d \vec{r} \text{ is path independent}$$
$$\text{Potential Function: If }\vec{F}=\nabla f \text{ then } f \text{ is the potential function for }\vec{F}$$
$$\vec{F} \text{ is conservative if and only if } \vec{F} \text{ is a gradient field }\nabla f \text{ for differentiable function }f$$
$$\vec{F}\text{ is conservative if and only if }\frac{\partial{P}}{\partial{y}}=\frac{\partial{N}}{\partial{z}},\frac{\partial{M}}{\partial{z}}=\frac{\partial{P}}{\partial{x}} \text{ and } \frac{\partial{N}}{\partial{x}}=\frac{\partial{M}}{\partial{y}}$$  
$$\text{For a conservative vector field, } \vec{F}, \int_C \vec{F} \cdot d \vec{r}=f(B)-f(A)$$
$$\oint{\vec{F} \cdot d \vec{r}}=0\Leftrightarrow  \text{The field }\vec{F}\text{ is conservative on }D$$
$$\text{Differential form: } M(x,y,z)dx+N(x,y,z)dy+P(x,y,z)dz$$
$$\text{Exact form: }Mdx+Ndy+Pdz=\frac{\partial f}{\partial x}dx+\frac{\partial f}{\partial y}dy+\frac{\partial f}{\partial z}dz=df  \text{ (} \vec{F}\text{ is conservative)}$$
$$\text{Circulation density (k-component of curl): }(\text{curl }\vec{F})\cdot\vec{k}=\frac{\partial{N}}{\partial{x}}-\frac{\partial{M}}{\partial{y}}$$
$$\text{Flux density (divergence): }\text{div }\vec{F}=\frac{\partial{M}}{\partial{x}}+\frac{\partial{N}}{\partial{y}}$$
$$\text{Green's Theorem:}$$
$$\text{Circulation-Curl (counterclockwise circulation): }\oint_C{\vec{F}\cdot\vec{T}}ds=\iint_R\left(\frac{\partial{N}}{\partial{x}}-\frac{\partial{M}}{\partial{y}}\right)dxdy$$
$$\text{Flux Divergence (outward flux of F): }\oint_C{\vec{F}\cdot\vec{n}}ds=\iint_R\left(\frac{\partial{M}}{\partial{x}}+\frac{\partial{N}}{\partial{y}}\right)dxdy$$
$$\text{Area of R}=\frac{1}{2}\oint{x}dy-{y}dx$$
$$\text{Surface Area:}$$
$$SA=\iint_S d\sigma$$
$$d\sigma=||\vec{r_u}\times\vec{r_v}||dudv=\frac{||\nabla{F}||}{\nabla{F}\cdot\vec{p}}dA=\sqrt{{f_x}^2+{f_y}^2+1}dxdy$$
$$\text{Surface Integral:}$$
$$\iint_S G(x,y,z)d\sigma$$
$$\text{Surface integral of F over S (Flux): }\iint_S \vec{F}\cdot\vec{n}d\sigma=\iint_S \vec{F}\cdot(\vec{r_u}\times\vec{r_v})dudv$$
$$\text{Mass (Thin shell)}= \iint_S \delta d\sigma$$
$$\text{First Moments (Thin shell):}$$
$$M_{yz}= \iint_S x \delta d\sigma$$		$$M_{xz}= \iint_S y \delta d\sigma$$		$$M_{xy}= \iint_S z \delta d\sigma$$
$$\text{Moment of inertia (Thin shell):}$$
$$I_x=\iint_S(y^2+z^2) \delta d\sigma$$		$$I_y=\iint_S(x^2+z^2) \delta d\sigma$$		$$I_z=\iint_S(x^2+y^2) \delta d\sigma$$		$$I_L=\iint_S r^2 \delta d\sigma \text{ where r(x,y,z) = distance from point (x,y,z) to line L}$$
$$\text{The del operator: }\nabla=\vec{i}\frac{\partial}{\partial{x}}+\vec{j}\frac{\partial}{\partial{y}}+\vec{k}\frac{\partial}{\partial{z}}$$
$$\text{curl }\vec{F}=\nabla \times \vec{F}$$		$$\text{div }\vec{F}=\nabla \cdot \vec{F}$$
$$\text{Important properties: curl(grad }{f})=\nabla \times \nabla {f}=\vec{0}$$,	$$\text{div(curl }\vec{F})=\nabla \cdot (\nabla \times \vec{F})=0$$
$$\text{Stoke's Theorem and Divergence Theorem:}$$
$$\text{Circulation of }\vec{F}=\text{Flux of curl }\vec{F}\text{: }\oint_C{\vec{F}}\cdot d\vec{r}=\iint_S(\nabla \times \vec{F})\cdot\vec{n} d\sigma$$
$$\nabla \times \vec{F}=\vec{0} \text{ at every point } \Leftrightarrow \oint_C \vec{F}\cdot d\vec{r}=0 \Leftrightarrow \text{ The field } f \text{ is conservative}$$
Outward flux of $\vec{F}$ along surface $S=\iint_S\vec{F}\cdot \vec{n} d \sigma = \iiint_D(\nabla \cdot \vec{F})dV$
