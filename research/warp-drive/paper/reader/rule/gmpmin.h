// gmpmin.h: the GMP interface the rule uses.  The real <gmp.h> is used when it is installed; otherwise the few
// declarations below are given directly (they are GMP's stable public ABI: mpz_t is {int alloc; int size; limb* d},
// the functions are exported as __gmpz_* / __gmpn_*).  Link with -lgmp (or -l:libgmp.so.10 where only the runtime
// library is present).
#pragma once
#if __has_include(<gmp.h>) && !defined(RULE_GMPMIN)
#include <gmp.h>
#else
// The declarations below are GMP's ABI on LP64 platforms (long and unsigned long of 64 bits), and only there.
static_assert(sizeof(long) == 8 && sizeof(unsigned long) == 8, "gmpmin.h's fallback GMP declarations are for LP64 only; install gmp.h");
#include <cstddef>
extern "C" {
typedef unsigned long mp_limb_t;
typedef long mp_size_t;
typedef unsigned long mp_bitcnt_t;
typedef struct { int _mp_alloc; int _mp_size; mp_limb_t* _mp_d; } __mpz_struct;
typedef __mpz_struct mpz_t[1];
typedef __mpz_struct* mpz_ptr;
typedef const __mpz_struct* mpz_srcptr;
void __gmpz_init(mpz_ptr);
void __gmpz_clear(mpz_ptr);
void __gmpz_set(mpz_ptr, mpz_srcptr);
void __gmpz_set_si(mpz_ptr, long);
void __gmpz_set_ui(mpz_ptr, unsigned long);
int __gmpz_set_str(mpz_ptr, const char*, int);
char* __gmpz_get_str(char*, int, mpz_srcptr);
void __gmpz_add(mpz_ptr, mpz_srcptr, mpz_srcptr);
void __gmpz_sub(mpz_ptr, mpz_srcptr, mpz_srcptr);
void __gmpz_mul(mpz_ptr, mpz_srcptr, mpz_srcptr);
void __gmpz_mul_si(mpz_ptr, mpz_srcptr, long);
void __gmpz_addmul(mpz_ptr, mpz_srcptr, mpz_srcptr);
void __gmpz_neg(mpz_ptr, mpz_srcptr);
void __gmpz_abs(mpz_ptr, mpz_srcptr);
void __gmpz_mul_2exp(mpz_ptr, mpz_srcptr, mp_bitcnt_t);
void __gmpz_fdiv_q_2exp(mpz_ptr, mpz_srcptr, mp_bitcnt_t);
void __gmpz_fdiv_q(mpz_ptr, mpz_srcptr, mpz_srcptr);
void __gmpz_tdiv_q(mpz_ptr, mpz_srcptr, mpz_srcptr);
void __gmpz_divexact(mpz_ptr, mpz_srcptr, mpz_srcptr);
void __gmpz_pow_ui(mpz_ptr, mpz_srcptr, unsigned long);
void __gmpz_ui_pow_ui(mpz_ptr, unsigned long, unsigned long);
void __gmpz_lcm_ui(mpz_ptr, mpz_srcptr, unsigned long);
int __gmpz_cmp(mpz_srcptr, mpz_srcptr);
int __gmpz_cmp_si(mpz_srcptr, long);
size_t __gmpz_sizeinbase(mpz_srcptr, int);
void __gmpz_sqrt(mpz_ptr, mpz_srcptr);
void* __gmpz_export(void*, size_t*, int, size_t, int, size_t, mpz_srcptr);
void __gmpz_import(mpz_ptr, size_t, int, size_t, int, size_t, const void*);
void __gmpn_tdiv_qr(mp_limb_t*, mp_limb_t*, mp_size_t, const mp_limb_t*, mp_size_t, const mp_limb_t*, mp_size_t);
mp_size_t __gmpn_sqrtrem(mp_limb_t*, mp_limb_t*, const mp_limb_t*, mp_size_t);
}
#define mpz_init __gmpz_init
#define mpz_clear __gmpz_clear
#define mpz_set __gmpz_set
#define mpz_set_si __gmpz_set_si
#define mpz_set_ui __gmpz_set_ui
#define mpz_set_str __gmpz_set_str
#define mpz_get_str __gmpz_get_str
#define mpz_add __gmpz_add
#define mpz_sub __gmpz_sub
#define mpz_mul __gmpz_mul
#define mpz_mul_si __gmpz_mul_si
#define mpz_addmul __gmpz_addmul
#define mpz_neg __gmpz_neg
#define mpz_abs __gmpz_abs
#define mpz_mul_2exp __gmpz_mul_2exp
#define mpz_fdiv_q_2exp __gmpz_fdiv_q_2exp
#define mpz_fdiv_q __gmpz_fdiv_q
#define mpz_tdiv_q __gmpz_tdiv_q
#define mpz_divexact __gmpz_divexact
#define mpz_pow_ui __gmpz_pow_ui
#define mpz_ui_pow_ui __gmpz_ui_pow_ui
#define mpz_lcm_ui __gmpz_lcm_ui
#define mpz_cmp __gmpz_cmp
#define mpz_cmp_si __gmpz_cmp_si
#define mpz_sizeinbase __gmpz_sizeinbase
#define mpz_sqrt __gmpz_sqrt
#define mpz_export __gmpz_export
#define mpz_import __gmpz_import
#define mpn_tdiv_qr __gmpn_tdiv_qr
#define mpn_sqrtrem __gmpn_sqrtrem
#define mpz_sgn(z) ((z)->_mp_size < 0 ? -1 : (z)->_mp_size > 0)
#endif

// The rule passes arrays of uint64_t to GMP's mpn functions as limb arrays: GMP must have 64-bit limbs.
static_assert(sizeof(mp_limb_t) == 8, "the rule needs a GMP with 64-bit limbs");

// A small owning wrapper (no operators: every operation is spelled out).
struct Z {
  mpz_t v;
  Z() { mpz_init(v); }
  explicit Z(long a) { mpz_init(v); mpz_set_si(v, a); }
  Z(const Z& o) { mpz_init(v); mpz_set(v, o.v); }
  Z& operator=(const Z& o) { if (this != &o) mpz_set(v, o.v); return *this; }
  ~Z() { mpz_clear(v); }
};
