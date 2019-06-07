using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemyAnimator : MonoBehaviour
{
    public Animator anim;

    public void Walk(bool walk)
    {
        anim.SetBool("Walk", walk);
    }
    public void Run(bool run)
    {
        anim.SetBool("Run", run);
    }
    public void Attack(bool Attack)
    {
        anim.SetTrigger("Attack");
    }
    public void Die(bool Die)
    {
        anim.SetBool("Die", Die);
    }
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
