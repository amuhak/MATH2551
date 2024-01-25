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
Line through $P(p_0,p_1,p_2)$ and parallel to $\vec{v}=a\vec{i}+b\vec{j}+c\vec{k}$: 
$$x=at+p_0 \quad y=bt+p_1 \quad z=ct+p_2$$
$$\langle at+p_0,bt+p_1,ct+p_3 \rangle=\langle a,b,c\rangle t+\langle p_0,p_1,p_2\rangle \forall -\infty<t<\infty$$
Distance between line and point $Q: d=\dfrac{||\vec{PQ}\times\vec{v}||}{||\vec{v}||}$
Line through $P(p_0,p_1,p_2)$ and perpendicular to $\vec{n}=a\vec{i}+b\vec{j}+c\vec{k}:$
$$a(x-p_0)+b(y-p_1)+c(z-p_3)=0$$
Angle between planes: $\theta=\cos^{-1}{\left(\left|\dfrac{\vec{n_1}\cdot\vec{n_2}}{||\vec{n_1}||\cdot||\vec{n_2}||}\right|\right)}$
Distance between Point $S$ and a plane: $d=\left|\vec{PS}\cdot\dfrac{\vec{n}}{||\vec{n}||}\right|$
$$\left\|\int_a^b\vec{f}(t)d{t}\right\|\leq\int_a^b\|\vec{f}(t)\|d{t}$$
$$
\begin{aligned}L&=\int_a^b\sqrt{\left(\frac{dx}{dt}\right)^2+\left(\frac{dy}{dt}\right)^2+\left(\frac{dz}{dt}\right)^2}dt&=\int_a^b||\vec{r}'(t)||dt \\
s(t)&=\int_{t_0}^t\sqrt{\left(\frac{dx}{d\tau}\right)^2+\left(\frac{dy}{d\tau}\right)^2+\left(\frac{dz}{d\tau}\right)^2}d\tau&=\int_{t_0}^t||\vec{r}'(\tau)||d\tau \end{aligned}$$
$$\frac{ds}{dt}=||\vec{v}(t)||$$
$$\vec{T}(t)=\frac{\vec{r}'(t)}{||\vec{r}'(t)||}=\frac{\vec{v}(t)}{||\vec{v}(t)||}$$
$$\kappa=\left\|\frac{d\vec{T}}{ds}\right\|=\frac{||\vec{T}'(t)||}{||\vec{r}'(t)||}=\frac{||\vec{r}'(t)\times\vec{r}''(t)||}{||\vec{r}'(t)||^3}$$
$$p=\frac{1}{\kappa}$$
$$\vec{N}(t)=\frac{\vec{T}'(t)}{||\vec{T}'(t)||}$$
$$\vec{B}(t)=\vec{T}(t)\times\vec{N}(t)$$
$$\vec{a}=a_T\vec{T}+a_N\vec{N}$$
$$a_t=\frac{d^2s}{dt^2}=\frac{d}{dt}||\vec{r}'(t)||$$
$$a_N=||\vec{T}'(t)||\cdot\frac{ds}{dt}=\kappa\left(\frac{ds}{dt}\right)^2=\kappa||\vec{r}'(t)||^2=\sqrt{||\vec{a}||^2-a_T^2}$$
$$||\vec{a}||^2=a_T^2+a_N^2$$
$$\tau=\frac{-d\vec{B}}{ds}\cdot\vec{N}'(t)=\frac{\begin{vmatrix} \dot{x}& \dot{y} & \dot{z}\\
\ddot{x} & \ddot{y} & \ddot{z}\\
\dddot{x} & \dddot{y} & \dddot{z}  \end{vmatrix}}{||\vec{r}'(t)\times\vec{r}''(t)||^2}=\frac{\vec{r}'(t)\cdot(\vec{r}''(t)\times\vec{r}'''(t))}{||\vec{r}'(t)\times\vec{r}''(t)||^2}$$
## Projectile Motion:
$\text{Max Height} = \frac{(v_0 \sin(\theta))^2}{2g}$
$\text{Range} = \frac{v_0^2 \sin(2\theta)}{g}$
$\text{Flight Time} = \frac{2v_0 \sin(\theta)}{g}$
## Polar and cylindrical equations:
$$
\begin{aligned}
\vec{u_{r}} &= \cos{\theta}\vec{i} + \sin{\theta}\vec{j} \\
\vec{u_{\theta}} &= -\sin{\theta}\vec{i} + \cos{\theta}\vec{j} \\
\vec{r}(t) &= r\vec{u_r} \\
\vec{r}'(t) &= \dot{r}\vec{u_r} + r\dot{\theta}\vec{u_{\theta}} \\
\vec{r}''(t) &= (\ddot{r} - r\dot{\theta}^2)\vec{u_r} + (r\ddot{\theta} + 2\dot{r}\dot{\theta})\vec{u_{\theta}} \\
\vec{r}(t) &= r\vec{u_r} + z\vec{k} \\
\vec{r}'(t) &= \dot{r}\vec{u_r} + r\dot{\theta}\vec{u_{\theta}} + \dot{z}\vec{k} \\
\vec{r}''(t) &= (\ddot{r} - r\dot{\theta}^2)\vec{u_r} + (r\ddot{\theta} + 2\dot{r}\dot{\theta})\vec{u_{\theta}} + \ddot{z}\vec{k} \\
\end{aligned}
$$
