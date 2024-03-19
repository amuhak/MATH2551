Fubini's Theorem 
$$V=\iint_R{f(x,y)}dA=\int_c^d{\int_a^b{f(x,y)}}dxdy=\int_a^b{\int_c^d{f(x,y)}}dydx$$
if $R$ is defined by $a\leq x \leq b$ and $g_1(x) \leq y \leq g_2(x)$ then,
$$V=\int_a^b{\int_{g_1(x)}^{g_2(x)}{f(x,y)}}dydx$$
Notice: The functions $g_n(x)$ are evaluated first.
# Properties
$$
\begin{align*}
\iint_R{cf(x,y)}dA&=c\iint_R{f(x,y)}dA \\
\iint_R{f(x,y) \pm g(x,y)}dA&=\iint_R{f(x,y)}dA \pm \iint_R{g(x,y)}dA \\
\iint_R{f(x,y)}dA &\geq 0 \text{ if } f(x,y) \geq 0 \text{ on } R \\
\iint_R{f(x,y)}dA &\geq \iint_R{g(x,y)}dA \text{ if } f(x,y) \geq g(x,y) \text{ on } R \\ 
\end{align*}
$$
If $R_1$ and $R_2$ are non-overlapping regions, 
$$\iint_R{f(x,y)}dA=\iint_{R_1}{f(x,y)}dA+\iint_{R_2}{f(x,y)}dA$$
$$A=\iint_RdA=\int_{x_1}^{x_2}\int_{y_1}^{y_2}dydx=\int_{\theta_1}^{\theta_2}\int_{r_1}^{r_2}r\ drd \theta$$
$$V=\iint_R{f(x,y)}dA$$
$$\text{Average Value}=\frac{1}{\text{Area of }R}\iint_R{f}dA \quad \text{ OR } \quad \frac{1}{\text{Volume of }D}\iiint_D{F}dV$$
$$
\begin{aligned}
V &=\iiint_DdV \\ 
&=\int_{x_1}^{x_2}\int_{y_1}^{y_2}\int_{z_1}^{z_2}dzdydx \\
&=\int_{\theta_1}^{\theta_2}\int_{r_1}^{r_2}\int_{z_1}^{z_2}r \ dzdrd \theta \\
&=\int_{\rho_1}^{\rho_2}\int_{\phi_1}^{\phi_2}\int_{\theta_1}^{\theta_2} \rho^2 \sin(\phi) \ \ d \theta d \phi d \rho
\end{aligned}
$$
## Mass and First Moments
### 3D Solids
$\delta$ is the density function.
$$
\begin{array} \\
\displaystyle \text{Mass: }M=\iiint_D{\delta}\ dV \\
\displaystyle \text{First Moments: }M_{yz}=\iiint_D{x\delta}\ dV, M_{xz}=\iiint_D{y\delta}\ dV, M_{xy}=\iiint_D{z\delta}\ dV\\
\displaystyle\text{Center of mass: }\bar{x}=\frac{M_{yz}}{M}, \bar{y}=\frac{M_{xz}}{M}, \bar{z}=\frac{M_{xy}}{M}\\
\end{array}
$$
### 2D Plates
$$
\begin{array} \\
  \displaystyle  \text{Mass: }M=\iint_R{\delta}\ dA \\
  \displaystyle  \text{First Moments: }M_{y}=\iint_R{x\delta}\ dA, M_{x}=\iint_R{y\delta}\ dA \\ 
  \displaystyle  \text{Center of mass: }\bar{x}=\frac{M_{y}}{M},\bar{y}=\frac{M_{x}}{M} \\
\end{array}
$$
## Moments of Inertia 
### 3D Solids
$$
\begin{aligned}
    \text{About x-axis: }I_x&=\iiint_D{(y^2+z^2)\delta}dV \\ 
    \text{About y-axis: }I_y&=\iiint_D{(x^2+z^2)\delta}dV \\ 
    \text{About z-axis: }I_z&=\iiint_D{(x^2+y^2)\delta}dV \\ 
    \text{About a line L: }I_L&=\iiint_D{r^2(x,y,z)\delta}dV \\
\end{aligned}
$$
### 2D Plates
$$
\begin{aligned}
    \text{About x-axis: }I_x&=\iint_R{y^2\delta}dA \\
    \text{About y-axis: }I_y&=\iint_R{x^2\delta}dA \\
    \text{About a line L: }I_L&=\iint_R{r^2(x,y)\delta}dA \\
    \text{About the origin: }I_O&=\iint_R{(x^2+y^2)\delta}dA=I_x+I_y \\
\end{aligned}
$$
## Joint probability density function
### Conditions
$$
\begin{align}
    f(x,y) &\geq 0 \\
    \int_{-\infty}^{\infty}\int_{-\infty}^{\infty}f(x,y)dxdy&=1 \\
    P((X,Y) \in R) &= \iint_R f(x,y) dxdy\\
\end{align}
$$
### Mean and expected value
$$
\begin{aligned}
\mu_X&=\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}xf(x,y)dxdy \\
\mu_Y&=\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}yf(x,y)dxdy
\end{aligned}
$$
## Cylindrical Coordinates $(r,\theta,z)$
$$
\begin{aligned}
    x &= r \cos{\theta} \\
    y &= r \sin{\theta} \\
    z &= z \\
    r^2 &= x^2+y^2 \\
    \tan{\theta} &= \frac{y}{x} \\
    \iiint_T \ dV &= \iiint r \ drd\theta dz
\end{aligned}
$$
## Spherical Coordinates $(\rho, \phi, \theta)$
$$
\begin{aligned}
r&=\rho \sin(\phi) \\ 
x&= r \cos(\theta)=\rho \sin(\phi)\cos(\theta)\\ 
y&= r \sin(\theta)=\rho \sin(\phi)\sin(\theta) \\
z&=\rho \cos(\phi) \\
\rho &= \sqrt{x^2+y^2+z^2} = \sqrt{r^2+z^2} \\
\iiint_T \ dV &= \iiint \rho^2 \sin{\phi} \ d\rho d\phi d\theta
\end{aligned}
$$
## Jacobian
$$J(u,v)=\begin{vmatrix} \frac{\partial{x}}{\partial{u}} & {\frac{\partial{x}}{\partial{v}}} \\
 \frac{\partial{y}}{\partial{u}} & \frac{\partial{y}}{\partial{v}} \end{vmatrix}=\frac{\partial(x,y)}{\partial(u,v)}$$
$$\iint_R{f(x,y)}dxdy=\iint_G{f(g(u,v),h(u,v))} \left | \frac{\partial(x,y)}{\partial(u,v)}\right | dudv$$
$$J(u,v,w)=\begin{vmatrix} \frac{\partial{x}}{\partial{u}} & \frac{\partial{x}}{\partial{v}} & \frac{\partial{x}}{\partial{w}} \\
 \frac{\partial{y}}{\partial{u}} & \frac{\partial{y}}{\partial{v}} & \frac{\partial{y}}{\partial{w}} \\
\frac{\partial{z}}{\partial{u}} & \frac{\partial{z}}{\partial{v}} & \frac{\partial{z}}{\partial{w}} \end{vmatrix}= \frac{\partial(x,y,z)}{\partial(u,v,w)}$$
$$\iiint_D{f(x,y,z)}dxdydz=\iiint_B{f(g(u,v,w),h(u,v,w),k(u,v,w)) \left | \frac{\partial(x,y,z)}{\partial(u,v,w)} \right | }dudvdw$$
