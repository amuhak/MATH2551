Credit Aarush Magic
$$\vec{a} \cdot \vec{b} = a_1 b_1 + a_2 b_2 + a_3 b_3 + \dots + a_n b_n$$
$$
\begin{aligned}
\vec{a} \times \vec{b} &=
\begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\
a_1 & a_2 & a_3\\
b_1 & b_2 & b_3  \end{vmatrix}\\ &= 
\begin{bmatrix}
u_2 & u_3 \\
v_2 & v_3
\end{bmatrix} \mathbf{i} -
\begin{bmatrix}
u_1 & u_3 \\
v_1 & v_3 
\end{bmatrix} \mathbf{j} + 
\begin{bmatrix}
u_1 & u_2 \\
v_1 & v_2
\end{bmatrix} \mathbf{k} \\
&=(a_2b_3-b_2a_3)\vec{i}-(a_1b_3+b_1a_3)\vec{j}+(a_1b_2+b_1a_2)\vec{k}
\end{aligned}
$$
## Properties:
$$

\begin{align*}
{\vec{u}} \cdot ({\vec{v}} \times {\vec{w}}) &= 
\begin{vmatrix}
    u_1 & u_2 & u_3 \\
    v_1 & v_2 & v_3 \\
    w_1 & w_2 & w_3 
\end{vmatrix}\\

\vec{a} \cdot \vec{b} &= \vec{b} \cdot \vec{a}\\

\vec{a} \times \vec{b}&= -\vec{b} \times \vec{a}\\

\vec{a} \cdot \vec{b} &= |\vec{a}| \cdot |\vec{b}|\cos(\theta)\\

|\vec{a} \times \vec{b}| &= |\vec{a}| \cdot |\vec{b}|\sin(\theta)\\

\vec{a} \cdot (\vec{b}+\vec{c}) &= \vec{a} \cdot \vec{b}+\vec{a}\cdot\vec{c}\\

\vec{a} \times (\vec{b}+\vec{c}) &= \vec{a} \times \vec{b}+\vec{a}\times\vec{c}\\

\vec{a} \cdot \vec{0} &= 0\\

\vec{a} \times \vec{0} &= \vec{0}\\

(c\vec{a})\cdot\vec{b}&=\vec{a}\cdot(c\vec{b})\\

(c\vec{a})\times\vec{b}&=\vec{a}\times(c\vec{b})\\

\vec{a}\cdot\vec{a}&=||\vec{a}||^2\\

\vec{a}\times\vec{a}&=\vec{0}\\

\text{If }\vec{a}\perp\vec{b}\text{ then }\vec{a}\cdot\vec{b}&=0\\

\text{If }\vec{a}\parallel\vec{b}\text{ then }\vec{a}\times\vec{b}&=\vec{0}\\

\vec{u}\times(\vec{v}\times\vec{w})&=(\vec{u}\cdot\vec{w})\vec{v}-(\vec{u}\cdot\vec{v})\vec{w}  \\

\end{align*}

$$

## Graphs
Cylinder: $ax^n+by^m=c,ax^n+bz^m=c,ay^n+bz^m=c$
Elliptical Paraboloid: $\frac{x^2}{a^2}+\frac{y^2}{b^2}=\frac{z}{c}$
Elliptical Cone: $\frac{x^2}{a^2}+\frac{y^2}{b^2}=\frac{z^2}{c^2}$
Ellipsoid: $\frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}=1$
Hyperboloid of 1 sheet: $\frac{x^2}{a^2}+\frac{y^2}{b^2}-\frac{z^2}{c^2}=1$
Hyperboloid of 2 sheets: $-\frac{x^2}{a^2}-\frac{y^2}{b^2}+\frac{z^2}{c^2}=1$
Hyperbolic Paraboloid: $-\frac{x^2}{a^2}+\frac{y^2}{b^2}=\frac{z}{c}, c>0$
## Other Formulas 
Line through $P(p_1,p_2,p_3)$ and parallel to $\vec{v}=a\vec{i}+b\vec{j}+c\vec{k}$: 
$$x=at+p_1 \quad y=bt+p_2 \quad z=ct+p_3$$
$$\langle at+p_1,bt+p_2,ct+p_3 \rangle=\langle a,b,c\rangle t+\langle p_1,p_2,p_3\rangle \text{ }\forall \text{ } t \in \mathbb{R}$$
Distance between line and point: 
$$d=\dfrac{||\vec{PQ}\times\vec{v}||}{||\vec{v}||}$$
Distance from a Point to a Plane,
$$d=\left| \vec{PS} \cdot \dfrac{n}{||n||} \right|$$
Projection, 
$$
\text{proj}_b a = \left( \dfrac{a \cdot b}{||b||} \right) \dfrac{b}{||b||}
$$
Line through $P(p_1,p_2,p_3)$ and perpendicular to $\vec{n}=a\vec{i}+b\vec{j}+c\vec{k}:$
$$a(x-p_1)+b(y-p_2)+c(z-p_3)=0$$
Angle between planes: 
$$\theta=\cos^{-1}{\left(\left|\dfrac{\vec{n_1}\cdot\vec{n_2}}{||\vec{n_1}||\cdot||\vec{n_2}||}\right|\right)}$$
Distance between Point $S$ and a plane: 
$$d=\left|\vec{PS}\cdot\dfrac{\vec{n}}{||\vec{n}||}\right|$$
The triangle property of integrals:
$$\left\|\int_a^b\vec{f}(t)d{t}\right\|\leq\int_a^b\|\vec{f}(t)\|d{t}$$
Arc Length $(s(t))$:
$$
\begin{aligned}L&=\int_a^b\sqrt{\left(\frac{dx}{dt}\right)^2+\left(\frac{dy}{dt}\right)^2+\left(\frac{dz}{dt}\right)^2}dt&=\int_a^b||\vec{r}'(t)||dt \\
s(t)&=\int_{t_0}^t\sqrt{\left(\frac{dx}{d\tau}\right)^2+\left(\frac{dy}{d\tau}\right)^2+\left(\frac{dz}{d\tau}\right)^2}d\tau&=\int_{t_0}^t||\vec{r}'(\tau)||d\tau \end{aligned}$$
Speed: 
$$\frac{ds}{dt}=||\vec{v}(t)||$$
The unit tangent vector $(T(t))$:
$$\vec{T}(t)=\frac{\vec{r}'(t)}{||\vec{r}'(t)||}=\frac{\vec{v}(t)}{||\vec{v}(t)||}$$
The curvature function $(\kappa(t))$:
$$
\begin{align*}
\kappa &= \left\|\frac{d\vec{T}}{ds}\right\| \text{ $T$ is the unit tangent vector, $s$ is the arc length } \\
&= \frac{||\vec{T}'(t)||}{||\vec{v}(t)||} \quad \text{ note: $\frac{ds}{dt} = ||v||$}\\
&= \frac{||\vec{r}'(t)\times\vec{r}''(t)||}{||\vec{r}'(t)||^3} \\
\end{align*}
$$
Radius of curvature:
$$p=\frac{1}{\kappa}$$
Principal Normal Vector $(N(t))$:
$$\vec{N}(t)=\frac{\vec{T}'(t)}{||\vec{T}'(t)||}$$
Binormal vector $(B(t))$:
$$\vec{B}(t)=\vec{T}(t)\times\vec{N}(t)$$
## Projectile Motion:
$\text{Max Height} = \frac{(v_0 \sin(\theta))^2}{2g}$
$\text{Range} = \frac{v_0^2 \sin(2\theta)}{g}$
$\text{Flight Time} = \frac{2v_0 \sin(\theta)}{g}$
